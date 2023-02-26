image ctc = POVDisplayable("mod_assets/STUFF/ctc.png")

define CTC_OFFSET = 6.0

screen ctc(arg=None, **kwargs):
    showif not _preferences.afm_enable:
        add (arg or "ctc"):
            at transform:
                subpixel True
                alpha 0.0 xoffset CTC_OFFSET yoffset -CTC_OFFSET

                block:
                    easeout 0.8 alpha 0.8 xoffset 0.0 yoffset 0.0
                    easein 0.8 alpha 0.2 xoffset CTC_OFFSET yoffset -CTC_OFFSET
                    repeat

            align (0.8522, 0.994) xoffset 13.0 yoffset -10.0