init python:
    def add_calendar_description(desc, year=None, month=None, day=None, key=None):
        date = phone.system.get_date()

        if year is None: year = date.year
        if month is None: month = date.month
        if day is None: day = date.day

        if key is None: key = "mc"

        c = phone.calendar.get_calendar(year, month, key)
        c[day].description = desc

    calendar_descriptions = {
        "sleepover": _("""\
The sleepover went really well!

Everyone got to see some crazy stuff that I really don't think any of us were expecting. 
It's kinda amazing how different the club can be when you take them out of that environment."""), # im stuff

        None: (
            _("""\
Monika Rein invited me to her club.

I'm still a little blown away - She's ranked first in every subject she does, and she asked me - ME - to join her club? I write poetry for fun, not for anything serious.

I hope she isn't doing this to make fun of me..."""),
            _("""\
It wasn't a bluff.

Monika genuinely wants me there. If that'd been all that happened today, it'd have been eventful enough, but Sayori? I saw Sayori.
I saw Sayori, and she doesn't... 

She doesn't hate me.""")
        ),


        "natsuki": (
            _("""\
This club might not be such a bad idea, honestly. It's been kinda fun so far.
Plus, hanging out with Amelia always lifts my spirits. I should really invite her out more often, shouldn't I?

Now I'm just going to feel bad, damn..."""),
            _("""\
Sayori... God, I feel so stupid!
Me?! It was my fault!

Even if it wasn't, even if I had nothing to do with it... I shouldn't have left.

I could have prevented all of this.

Fuck..."""),
            _("""\
She called me jealous.

I wish I had a retort. I wish I'd done something, anything. Sayori deserves better than me.

Natsuki's been standing by her all this time. She's so much more deserving of that attention than I am."""),
            _("""\
I don't understand. She should hate me. She should loathe me for every second I spend in her life.

So why doesn't she? What did I do to deserve her back in my life?"""),
            _("""\
I've spent pretty much every day with Amelia this week.

I don't think we've done that since... probably since we were first-years? We both just got busy, I guess.

Thinking back on it, I think I've just now realised how much I missed it."""),
            _("""\
That was sure weird.

Who'd have thought the vice president of the student council would be so jumpy?
It makes sense, considering she has a manga collection, I suppose?

Kinda unsettling seeing these tropes in real life though."""),
            _("""\
Well, we finally talked about it, I guess.

After all this time, I guess it's just as well. I might not understand how she can somehow still care for me, but... I'm past the point of complaining.
If this is what she wants, I won't dare turn her down."""),
            _("""\
I swear to god, I'm having the weirdest dreams lately.

On the plus side, at least, they're just dreams? I'd rather that than the alternative, I guess... And who knew, that big tsundere act Natsuki's been putting on, once you dig past it, has a cute side.
It's kinda sweet, in a very... let's call it forward way."""),
            _("""\
Ah, that Ellen.

She's a bit of a rat when she wants to be. Hanging out with Amelia seems to have become a basically daily thing now, and combining that with the club, I've been awfully busy lately.

I hope I still have time for my studies..."""),
            _("""\
Natsuki... She's completely head over heels for Sayori.

I guess I should feel vindicated in my own feelings, if this were back in the day, but...
She was so completely willing to give all that up, so easily, if I'd said the word. She's so much more mature than I am, too.

It almost makes me sick to think about how I acted back then..."""),
        ),


        "monika": (
            _("""\
Monika's taste in literature is bemusing, and I'm still a little confounded by it all.
There's so much going on, all at once in this club that it's a little hard to keep track of.

One thing's for certain, though... Something seems to be troubling her, and I'm not sure if it's my place to reach out a helping hand."""),
            _("""\
Spending time with Sayori again has been like a dream.

Getting to interact with Monika has been something out of a fantasy.

Everything's been... I don't know how to describe it, but I feel like I don't deserve it."""),
            _("""\
What is happening today? God, it's like the perv fairy jabbed me.

How do I even look Amelia in the eye?"""),
            _("""\
I went on a date with Monika. THE Monika. And she had a nice night?

Do I - What do I do?
Does that mean anything?
Is she interested?
Am- Am I interested?"""),
            _("""\
Monika opened up to me today.
She trusted me enough to lean on me.

All this time, I've felt... Well, like I've been on the back foot, always playing catchup."""),
            _("""\
I'm such an idiot."""),
            _("""\
Monika really is just like me, in a lot of ways.
I put her on a pedestal, just like I did to Sayori all those years ago.

I'm just the worst."""),
            _("""\
Natsuki...

She's just in the next room. I know she was just screwing with me, but I don't think I've ever... Been so overtly flirted with before.

I'd better keep her away from alcohol from now on."""),
            _("""\
I'm so, so sorry, Monika. I'm such an idiot.

She deserves better."""),
            _("""\
She wants to spend time with me, to be my friend, but I don't know if I'm ready for that.

I don't know if I'm ready for anything, anymore..."""),
        ),


        "sayori": (
            _("""\
Everyone in this club is so welcoming and friendly.

It's amazing that it's taken me so long to really find people who want to spend time with me like this, outside of Amelia.
Not to mention...

Sayori. God, Sayori, she doesn't hate me. After all this time...

It feels like I'm walking on air."""),
            _("""\
How could I? How dare I?
Ventris deamonis.
Crudelis et prodigi.
Callosa.

How do I look Sayori in the eye again after this?

She doesn't deserve this.

She doesn't deserve to me around me."""),
            _("""\
She should hate me, the way I hate me.
But she doesn't.

She forgives, and it's more than I deserve.

I don't...
I don't know what I'd do without her."""),
            _("""\
Sayori wants me to chill, to relax, to not be so worked up.
Even if she doesn't say it, I can see it.

I still know what's going on in those eyes, even if I can't read her mind.

It feels like only yesterday that we stopped talking."""),
            _("""\
Why is it that every day I do something that hurts her?"""),
            _("""\
She kissed me.

Does she hate me that much?
I've been trying so hard to hide it, but this is Sayori.

She knows.

Of course she knows.
And if she knows, why would she do that?

To hurt me?
Why?"""),
            _("""\
We were drinking, then she kissed me again.

Was she using the alcohol as an excuse?
Does she really just want to hurt me?

There's no way that she..."""),
            _("""\
We spent all day together, and I had to go drop the ball again.

Every day.

Why? I don't know what's wrong with me! What do I want from her? What do I want from me?

She's my best friend, and all I can do is sit over here treating her like an object!"""),
            _("""\
I'm still floating.
She... We...

I've never felt like that, not when I do it myself.

Fuck..."""),
        ),

        "yuri": (
            _("""\
Yuri, the girl from my class, is quite possibly one of the most interesting people I've ever met - An absolute enigma.

She seems to want to befriend this Natsuki girl, the student council member. Maybe that'll help us all grow closer as a club?

Everyone else in the club she seems to know at least in passing, so it feels like that might be a good start.

As for me, I'm definitely interested in spending more time with her."""),
            _("""\
Yuri asked me to open up today, but I'm not so sure that's a good idea.
I still don't know her very well, and she seems to be unwilling to reciprocate.

I might give it some time; the last thing I want to do is lean on her if she's got things on her plate already..."""),
            _("""\
Maybe Yuri and Natsuki are closer than I first thought?

Natsuki seems almost protective of her.
It's kinda adorable, in a way."""),
            _("""\
I must seem stressed. Even Amelia's keeping tabs on me now.

Maybe I'm just not used to being this social..."""),
            _("""\
Getting to hang out with Sayori and Monika has to be a huge highlight of my week, I won't lie.

Sayori doesn't seem to hold anything against me, and Monika's less wound up outside of school.

I'm looking forward to what the next few weeks hold, honestly - Especially if Sayori's planning a sleepover."""),
            _("""\
Everyone's hiding something from me, when all I want to do is help.
Now Natsuki's hurt, and I can't do anything about that either."""),
            _("""\
I spent all day in bed.

Barely crawled out to get some painkillers and drown in the shower.
I guess the good news is I caught up on some sleep, but I didn't even have the energy to do any study, which is just...

How the hell am I going to keep up my grades if I'm sick?"""),
            _("""\
Look at me, god-damn flip-flopping all over the place.
I can't stick to one decision.

I just... Yuri's been opening up a little, and I really appreciate that.

Maybe being sick yesterday helped in some weird way?"""),
            _("""\
Yuri's been having panic attacks? That's why everyone's so worried?

That still doesn't explain what happened to Natsuki, or..."""),
            _("""\
Everything makes sense now.

It all just... God, I feel like such a monster for even thinking some of the things I have over the past week."""),
        )
    }