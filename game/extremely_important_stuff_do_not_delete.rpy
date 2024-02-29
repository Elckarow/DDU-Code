default persistent.stuff = 0

init python hide:
    @config.history_callbacks.append
    def count_stuff(h):
        persistent.stuff += h.what.lower().count("stuff")
