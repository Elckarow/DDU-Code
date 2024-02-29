image ctc = Null()

image phone_ctc:
    "gui/ctc.png"
    xoffset -5 alpha 0.0 subpixel True
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

define CTC_OFFSET = 6.0

# actual say ctc is in say_overlay
screen ctc(arg=None, **kwargs):
    if not _preferences.afm_enable:
        if phone.calls._current_caller is not None:
            add (arg or "phone_ctc"):
                subpixel True
                align (0.98, 0.98)
