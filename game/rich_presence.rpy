default persistent.discord_rpc = False
default discord_rpc_status = None

init python in discord_rpc:
    from renpy.store import (
        store, config, phone, persistent,
        is_recording, SetField, Function, Dialogue, invoke_in_thread, is_android
    )
    import time, pypresence
    _constant = True

    exceptions = (pypresence.exceptions.PyPresenceException, RuntimeError)

    if is_android():
        presence = None
    
    else:
        start_time = time.time()

        class DiscordPresence(renpy.python.NoRollback):
            presence = None

            def __new__(cls):
                if cls.presence is None:
                    cls.presence = self = renpy.python.NoRollback.__new__(cls)
    
                    self._old_status = ""

                    save_states_message = _("Managing the Save States")
                    settings_message = _("In the Settings")

                    self.screen_messages = (
                        ("ch_select", _("Choosing a Branch")),
                        ("gallery", _("Visiting the Gallery")),
                        ("load", save_states_message),
                        ("ig_file_slots", save_states_message),
                        ("extras", _("Exploring the Extras")),
                        ("main_menu", _("In the Main Menu")),
                        ("configuration", settings_message),
                        ("ig_configuration", settings_message),
                        ("character_preview", _("Learning More About the Characters")),
                        ("credits", _("Reading the Credits")),
                    )

                    self.presence = pypresence.Presence("1040341661617762345")

                    self.connected = False
                    self.connect()

                    config.interact_callbacks.append(self.per_interact)
                    config.quit_callbacks.append(self.shutdown)

                return cls.presence
            
            def connect(self):
                if not persistent.discord_rpc:
                    self.connected = False
                    return

                if self.connected:
                    return

                try:
                    self.presence.connect()
                    self.connected = True
                except exceptions:
                    self.connected = False
            
            def shutdown(self):
                if self.connected:
                    self.presence.close()
                self.connected = False
            
            def per_interact(self):  
                invoke_in_thread(self.update_status)

            def update_status(self):
                self.connect()

                if not self.connected:
                    return

                if is_recording():
                    status = __("Recording...")

                else:
                    for screen_name, message in self.screen_messages:
                        if renpy.get_screen(screen_name) is not None:
                            status = __(message)
                            break
                    else:
                        if not store.main_menu:
                            status = store.discord_rpc_status or phone.system.get_date().strftime("%d/%m/%Y")
                        else:
                            status = "unknown"

                if status != self._old_status:
                    try:
                        self._old_status = status
                        self.presence.update(
                            details=status,
                            start=start_time,
                            large_image="ddu_logo",
                            small_image="studiosilver",
                            large_text=__("This game is an unofficial fan game, unaffiliated with Team Salvato."),
                            small_text=__("A Studio Silver mod"),
                        )
                    except exceptions:
                        self.connected = False

            def TurnOn(self):
                return [
                    SetField(persistent, "discord_rpc", True),
                    Function(self.connect)
                ]

            def TurnOff(self):
                return [
                    SetField(persistent, "discord_rpc", False),
                    Function(self.shutdown)
                ]

        presence = DiscordPresence()

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
