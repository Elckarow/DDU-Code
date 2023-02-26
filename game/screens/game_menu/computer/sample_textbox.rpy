init python:
    class SampleText(renpy.text.text.Text):
        def __init__(self, text, **properties):
            self.backup_text = text

            properties["slow"] = True
            super(SampleText, self).__init__(text, **properties)

            self.set_loop_time()
        
        def set_loop_time(self):
            cps = float(_preferences.text_cps)
            l = float(len(self.text[0]))

            self.loop_time = (l / cps) + 1.0

        def call_slow_done(self, st):
            self.text = [ ]
            self.set_text(__(self.backup_text))
            self.set_loop_time()

        def render(self, width, height, st, at):
            return super(SampleText, self).render(width, height, st % self.loop_time, at % self.loop_time)

screen sample_textbox():
    style_prefix "sample_textbox"

    frame at Flatten:
        window:
            add SampleText(
                _("-Doki Doki Undercurrents-\nThe text in-game should look like this."),
                slow_cps=True, style="say_dialogue"
            )


style sample_textbox_frame is empty:
    background Crop(
            (   
                absolute((config.screen_width / 2) - (gui.sample_textbox_width / 2)),
                absolute((config.screen_height * gui.textbox_yalign) - gui.sample_textbox_height),
                gui.sample_textbox_width,
                gui.sample_textbox_height
            ),
            "bg club_day"
        )
        align (1.0, 0.0)

style sample_textbox_window is window:
    xysize (gui.sample_textbox_width, gui.sample_textbox_height)

style sample_textbox_text is say_dialogue

style below_sample_textbox:
    xsize gui.sample_textbox_width