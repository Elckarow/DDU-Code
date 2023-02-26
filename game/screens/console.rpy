default console.history = [ ]
default console._current_entry = None
default console._typing_indicator = True

init python in console:
    from renpy import store
    from store import _window_hide, pause, __, Dissolve, basestring

    CPS = 30
    CPS_DELAY = 0.6
    HISTORY_LENGHT = 20

    enter_transition = Dissolve(0.3)
    exit_transition = Dissolve(0.3)
    
    class _Entry(object):
        def __init__(self, entry):
            if not isinstance(entry, basestring): raise ValueError(f"expected str, got {entry.__class__.__name__}")
            self.entry = entry
    
    class Input(_Entry): pass
    class Output(_Entry): pass

    _yadjustment = renpy.display.behavior.Adjustment()
    
    def input(text, delay=-1, slow=True):
        entry = Input(text)
        _entry(entry, delay, slow)
    
    def output(text, delay=None, slow=False):
        entry = Output(text)
        _entry(entry, delay, slow)

    def show(transition=enter_transition, delay=0.4):
        if renpy.get_screen("console") is None:
            renpy.show_screen("console")
            if transition is not None:
                renpy.with_statement(transition)
            pause(delay)
    
    def hide(transition=exit_transition, delay=0.4):
        if renpy.get_screen("console") is not None:
            renpy.hide_screen("console")
            if transition is not None:
                renpy.with_statement(transition)
            pause(delay)

    def clean_history():
        global HISTORY_LENGHT
        while len(history) > HISTORY_LENGHT:
            history.pop(0)

    def clear_history():
        history.clear()
    
    def _get_time(entry):
        global CPS, CPS_DELAY
        return (len(renpy.filter_text_tags(__(entry.entry), deny=())) / CPS) + CPS_DELAY
    
    def _entry(entry, delay=None, slow=True):
        global _current_entry, _typing_indicator

        window_auto = store._window_auto
        _window_hide()

        history.append(entry)
        clean_history()      

        if slow:
            _current_entry = entry
            _typing_indicator = False
            pause(_get_time(entry))

        store._window_auto = window_auto
        _current_entry = None
        _yadjustment.value = float("inf")
        pause(delay)
        _typing_indicator = True

screen console():
    style_prefix "console"

    frame:
        viewport:
            draggable True
            mousewheel True
            yadjustment console._yadjustment
            yinitial 1.0

            vbox:
                for entry in console.history:
                    showif entry is not console._current_entry:
                        showif isinstance(entry, console.Input):
                            use _console_input():
                                text entry.entry
                        elif isinstance(entry, console.Output):
                            text entry.entry
                                
                    else:
                        showif isinstance(entry, console.Input):
                            use _console_input():
                                add renpy.display.layout.AdjustTimes(
                                        Text(
                                            entry.entry,
                                            style="console_text",
                                            slow_cps=console.CPS,
                                        ),
                                        None,
                                        None
                                    )
                        elif isinstance(entry, console.Output):
                            add renpy.display.layout.AdjustTimes(
                                    Text(
                                        entry.entry,
                                        style="console_text",
                                        slow_cps=console.CPS,
                                    ),
                                    None,
                                    None
                                )
                
                showif console._typing_indicator:
                    use _console_input():
                        text "_" bold True:
                            at transform:
                                alpha 1.0
                                pause 0.6
                                alpha 0.0
                                pause 0.6
                                repeat

screen _console_input():
    style_prefix "console"

    hbox:
        text ">>> " yoffset 1

        transclude

style console_frame:
    background Frame(Transform(Solid("#333"), alpha=0.75))
    xysize (480, 180)
    padding (7, 10, 20, 7)

style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []