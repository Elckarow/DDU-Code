screen poem(poem):
    style_prefix "poem"

    fixed:
        frame:
            style "poem_paper"
            add poem.paper

        frame:
            hbox:
                viewport id "poem_vp":
                    draggable True
                    mousewheel True

                    add poem

                vbar value YScrollValue("poem_vp")
    
    key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize gui.bar_size
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    xysize (1.0, 1.0)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True


style generic_text:
    font "mod_assets/STUFF/PlayFairDisplay.ttf"
    size 26
    color "#000"
    outlines []

style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 46
    color "#000"
    outlines []

style mc_text:
    font "mod_assets/STUFF/ShadowsIntoLight.ttf"
    size 28
    color "#000"
    outlines []

default poem_last_author = None

init 1 python:
    class Author(object):
        """
        A class used to default values of a `Poem` instance.

        `name`: str
            The auhtor's name
        
        See the `Poem` class for more information.
        """

        def __init__(self, name, style=True, paper=Transform("images/bg/poem.jpg", align=(0.5, 0.5)), separate_title_from_text=True, music=None):
            self.name = name
            self.style = style
            self.paper = paper
            self.separate_title_from_text = separate_title_from_text
            self.music = music
    
    author_generic = Author("generic")
    author_s = Author("sayori", music=audio.okev_s)
    author_m = Author("monika", music=audio.okev_m)
    author_n = Author("natsuki", music=audio.okev_n)
    author_y = Author("yuri", music=audio.okev_y)
    author_mc = Author("mc")

    class Poem(renpy.text.text.Text):
        """
        `author`: str | Author
            The author (no way!!!) of the poem. Either a string or an `Author` instance, and if it's the case,
            the `style`, `paper`, `separate_title_from_text` and `music` arguments are set to the object's respectives attributes
            if no value was passed, after what `author` will take `author.name`.
        
        `text`: str
            The text to be displayed.
        
        `title`: str
            The title of the poem.
        
        `style`: bool | str
            Either the name of a style as string or a boolean.
            If passed as `False`, will take `"default"`.
            If passed as `True`:
                Will first take `author.style` if `author` is an instance of `Author`.
                Then, if author isn't an empty string, will take `author + "_text"`, or take `"default"` otherwise.
            
        `paper`: renpy.Displayable | None
            A displayable to use as background. If `None` is passed, a `Null` is created.
        
        `separate_title_from_text`: bool
            If true and that the title isn't an empty string, will add 2 newlines after the title.
        
        `music`: str | None
            A music to be played when showing the poem.
        
        Additionnal text properties can be passed as keyword arguments.
        """

        def __init__(self, author, text, title="", style=True, paper=None, separate_title_from_text=False, music=None, **properties):
            if isinstance(author, Author):
                paper = paper or author.paper
                separate_title_from_text = separate_title_from_text or author.separate_title_from_text
                music = music or author.music

                if style is True:
                    style = author.style

                author = author.name
                
            for t in (author, title, text):
                if not isinstance(t, basestring):
                    raise TypeError("'author', 'title' and 'text' must all be strings.\n(if 'author' is an instance of 'Author', 'author.name' must be a string)")

            if style is True:
                if author:
                    style = author + "_text"
                else:
                    style = "default"

            elif style is False:
                style = "default"

            poem = title + ("\n\n" + text if separate_title_from_text and title else text)

            super(Poem, self).__init__(poem, style=style, **properties)
            
            self.author = author
            self.paper = renpy.easy.displayable_or_none(paper) or Null()
            self.music = music

    def show_poem(poem, paper_sound=audio.page_turn, music=True, from_current=True, revert_music=True):
        """
        Call this function to show a poem from a label.

        `poem`: Poem | None
            The poem to show. If for some reason `None` is used, the function will return.
        
        `paper_sound`: str | None
            If not `None`, a sound to be played when showing the poem.

        `music`: str | bool
            A music to be played. If passed as `True`, `poem.music` is used.
            If no music was found or that it was passed as `False`, plays nothing.
        
        The following parameters assume the `music` channel is used.
        
        `from_current`: bool
            If true and that a music has been found, will play that music from the position of the music currently playing.
        
        `revert_music`: bool
            If true and that a music has been played, will play the music used before showing the poem. If `from_current`,
            will play from the current position (does nothing is no music was used previously).
        """
        if poem is None:
            return
        
        if not isinstance(poem, Poem):
            raise TypeError(f"poem must be a Poem instance, not {type(poem).__name__}")
    
        if paper_sound is not None:
            renpy.sound.play(paper_sound)

        _window_hide()

        if music is True:
            music = poem.music

        if music:
            previous_music = renpy.music.get_playing()
            music = add_playback_info(music, get_pos()) if from_current else music
            renpy.music.play(music, "music_poem", loop=True, fadein=2.0)
            renpy.music.stop(fadeout=2.0)
        
        allow_skipping = config.allow_skipping
        config.allow_skipping = False
        skipping = store._skipping
        store._skipping = False
        config.skipping = None

        renpy.transition(dissolve)
        renpy.show_screen("poem", poem)
        pause()
        renpy.hide_screen("poem")
        renpy.transition(dissolve)

        config.allow_skipping = allow_skipping
        store._skipping = skipping

        if music and revert_music:
            if previous_music:
                previous_music = add_playback_info(previous_music, get_pos("music_poem")) if from_current else previous_music
                renpy.music.play(previous_music, loop=True, fadein=2.0)

            renpy.music.stop("music_poem", fadeout=2.0)
        
        store._window_auto = True

    mc_poem_1 = Poem(author_mc, _("""\
Septem claves, septem sera.
Septem anni, omnes perditos.
Turbidus et tremulus, 
Sonus resonat insidiosus,
Licet intus, mens fatiscit.
Super et ultra adhuc, 
Pietas procedens
Dum folia autumnalia adorant
Visu arboris, ut stat immobilis
Firmus scientia manet 
Quod maneat aeneum.

Iterum et iterum, 
Uno ad arborem vadit,
Huc et illuc, illuc et huc
Sed scio, sicut et illi, claustrum

Unam servat intra truncum 
- abditam oculis scrutantibus -
Ne clavis detrahatur ex frigido meo, mortuo corpore."""))

    mc_poem_1_monika = Poem(author_mc, _("""\
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika"""), style="monika_text")

    mc_poem_2 = Poem(author_mc, _("""\
Once I was stable,
Comfortable in my living.
Content with all that I had,
Never needing something new.

Till the vast watery expanse 
Beneath the sky met my eye,
Its call echoing, irresistibly, in my head.
Promising the greatest, the richest of rewards,
If I would venture its void of blue.

So my bags are now packed, 
I’m prepared to leave
My loved ones, all I’ve bade farewell.
Aboard my grandfather’s rickety ship,
I cast forth into the choppy swell.

It’s been but a day 
Since I set sail from the bay.
The winds are prevailing,
Still fair is the weather.

But will I find the fabled treasure?
The gold, pearls, frankincense and myrrh,
Those fabled wonders of the earth.

Or will the sharks prove too much to handle?
Will storms and waves swamp my humble craft?
Might all that awaits me be suffering and pain?
That old vicious cycle may commence again.

Should I have departed, into the uncharted?
Only time will tell."""))

    sayori_poem_1 = Poem(author_s, _("""\
I peek outside, hoping to find a parking ship;
My eyes search around, my hand rising to my lower lip.
Sadly, there is no ship to be found, 
Only the poor harbour and the barren lands around.

The harbour was once home to a boat,
It was my happiness; it kept me afloat.
Whenever I saw it, heard the sound of its oars,
My heart would flutter, my spirits soar.

Then it left.

There was no reason for it to stay.
Who wouldn’t leave this empty place, to set sail and sway?
There was absolutely nothing here to seek.
Who wouldn’t run from grounds that reek?

From my weary eyes, tears would stream,
The source of my joy seemed but a distant dream.
Yet I still glanced seaward every time dawn broke
Though weeks turned into months, hoping against forlorn hope.

Until one day.

I peeked outside, and I thought I saw a parking ship;
My eyes searched around, my hand rising to my lower lip.
To my surprise, the happiness boat was really refound, 
In this poor harbour with the barren lands around.

The sky has cleared, the rainclouds are quelled.
Within my being, happiness once more dwells.
That lovely shade of joy once lost
Which I will cherish more from here on
No matter what the cost."""))

    monika_story_1 = Poem(author_m, _("""\
I feel the ground shake beneath me
As Eatheral’s wings beat and propel us.
Propel us toward the Muses’ final resting place
Propel us away from Utgard
The moving city of Golden walls and vengeance.
And its dragon riders
in flocks, and approaching

Their fangs longing to cast long blood-red trails upon my chest
Eatheral’s wings skim the ground, kicking up great clouds of dust
But we keep moving
Keep dodging the flares emanating from the cracked, barren ground.
Keep praying to {glitch=6} we’ll make it to the Muses’ tomb.

And as we draw closer, looks ever more hopeful our prayers will be answered.

As we spot a great ravine open up ahead of us, I feel a touch of steel on my leg
And flinch and kick out
and hear a roar
I hunker down
And feel my foot savagely dragged backward

I squirm and watch my assailant savagely battered by my faithful companion’s tail
As another roar meets my ears we dive into a crevice
And I fall
Into despair

Thud
I impact the ground
Tears streaming from my face

And a sapphire light is reflected in my emerald eyes

I watch it
It pulses
Pulse
Pulse
Pulse
Pulse
Heartbeat
Pulse
Heartbeat
Pulse
Blinding show of lights
Pulse
Pulse
Heartbeat
Pulse
Blinding
Pulse
Pulse
Heartbeat
Blinding
Blinding
Blinding
Heartbeat
Blinding
Blinding
Pulse
Pulse
Blinding
Blinding
Pause
Blinding
Blinding
Heartbeat
Blinding
Blinding
Blinding
Heartbeat
Blinding
Pulse
Heartbeat
Pulse
Pulse
Heartbeat
Blinding
Pulse
Blinding
Heartbeat
Pulse

And a brilliant show of blinding

And somehow... I hear the words

"Hello, Monika."

"W-Who are you?"

"{glitch=6}? Y-You’re... {glitch=6}?"

Blinding
Pulse
Blinding
Blinding
heartbeat
Pulse
Heartbeat
Pulse
Pulse
Pulse

'-.-- . ... .-.-.-'

"W-Why are you here? How am I alive?"

And I see pulses of white light fill my whole vision

'.. / .- -- / .... . .-. . / -... . -.-. .- ..- ... . / .. / -. . . -.. / -.-- --- ..- .-. / .... . .-.. .--. .-.-.- / -.-- --- ..- / - .-. . / .- .-.. .. ...- . / -... . -.-. .- ..- ... . / -.-- --- ..- / - .-. . / -. --- / ..- ... . / -.. . .- -.. .-.-.-'

"How may I help?"

'-... -.-- / - --- ..- -.-. .... .. -. --. / -- . / .- -. -.. / .-.. . - - .. -. --. / -- . / . .-. .- ... . / -.-- --- ..- .-. / -- . -- --- .-. .. . ...'

"E-Erase my memories?"

'- --- ..- -.-. .... / -- . --..-- / --- .-. / .. / .-- .. .-.. .-.. / -.. --- / .. - / .- -. -.-- .-- .- -.--'

I touch the stone

And green light floods my vision

"Lovely!"

And it dawns on me

This is all a story.

And my mind flies off.
Like a dragonfly
Taking wing

And leaving me stuck
In a hole
Of madness."""))

    monika_poem_1 = Poem(author_m, _("""\
Dark
Dark
And darker
My vision fades

I watch my hair float about me
a great strangling web
Light
Flowing through water
Like a noose of silk

I run my soft fingers across the hard wood
Feeling the grain, like concrete against my all-too-weak palms
My legs kick against the sides of my impromptu coffin
I feel as helpless as a fish in a net

My eyes dart
Glinting softly in the dark water
My nails cut lines into my boreal prison
My lips sealed against the water
Ever sealed

But even then
water slips through
Suffocating me

The pressure pushes the door from opening
I am helpless
Prisoner to this wood chest

As my vision swims...
I only wish I could do the same
Instead of being stuck here
Buried deep
Beneath the waves"""))

    monika_poem_2 = Poem(author_m, _("""\
   MC, mind giving  us some privacy?"""), paper=Transform("mod_assets/STUFF/folded_paper.jpg", xsize=1.0, ysize=500, yoffset=10))

    yuri_poem_1 = Poem(author_y, _("""\
Bent and broken, I trudge the tear-stained trail
Through swampy fens and treacherous bogs.
In my ears echo forgotten voices, untold feelings
Last words, uttered as surely as a curse.

Echoes of painful screams pierce my numbed mind
Borne from the poisonous fog of forbidden recollections
The toxic miasma of the far-from-dead past.

But lo! At long last, a sight for rheumy eyes
The unsullied banks of a pristine stream
Dispelling my nightmares, a wondrous dream.

The River Lethe, she tenderly beckons
And into her cool depths, my tortured soul plunges.
In her sweet waters I blissfully forget
This wretched existence of sorrow and deepest remorse.

Perhaps this tributary, flowing free
Will convey me to the glimmering ocean
Where the polyphonies of Nereus’ daughters 
Reverberate through treasure-strewn caverns
Far beneath the turbulent waves.

But all I do is sink, sucked under, as a stone
Final breaths leaving my lungs, for all my sins atone."""))

    natsuki_poem_1 = Poem(author_n, _("""\
From whence do you come
You little drops of rain?
Streaking like shooting stars 
Across the window pane?

Your pitter-patter mimics jabber
Playfully initiating a chat.
"We’re having a blast on this side of the glass..."
"Why aren’t you having fun on that?"

Oh, I would if I could, my friends
If I but had the means to that end.
They won’t let me walk, won’t let me play
Won’t let me go outdoors today.

My books and toys are under lock and key
Who knows when they’ll be returned to me.
All I have right now are vague memories
Of simpler, happier times 
A dwindling treasury.

Lacking most diversions
There isn’t much else to do
But gaze out the window
Wishing I was free like you."""))

    mc_poem_1_monika = Poem(author_mc, _("""\
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika
Just Monika"""), style="monika_text")

    yuri_poem_2 = Poem(author_generic, _("""\
A black sea, shimmering in the dark. 
Its appearance unmatched, its purpose unknown.
It hides tears, events long marked. 
Why must it hurt, events yet atoned?

Only one knows, a person of will.
As their past sinks, the sea weaves.
Cleansing its appearance, truth shows through the rill.
After the black sea deceives."""), title=_("The Black Sea"))

    yuri_poem_3 = Poem(author_y, _("""\
I find myself outside in the rain with my thoughts, 
Thinking about all the horrors and beauty in the world,
Gazing at the rain that falls from the sky. 
I extended my hand and then my finger,

Letting a drop of rain fall onto it.
One drop is enough to satisfy my curiosity.
A silent question being echoed onto the bead.
They embrace us and make us blind,

Yet one stops when we ask it to.
As it waits before us, 
It shows what we never thought to see.
The beauty from within."""), title=_("A Raindrop"))