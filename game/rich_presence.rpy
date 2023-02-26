default persistent.discord_rpc = False

init python:
    if not renpy.android:
        class DiscordPresence(object):
            _presence = None

            @staticmethod
            def ready_callback(current_user):
                print('Our user: {}'.format(current_user))

            @staticmethod
            def disconnected_callback(codeno, codemsg):
                print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
                    codeno, codemsg
                ))

            @staticmethod
            def error_callback(errno, errmsg):
                print('An error occurred! Error {}: {}'.format(
                    errno, errmsg
                ))

            def __new__(cls, *args, **kwargs):
                if cls._presence is not None: raise Exception("Rich Presence already created")
                cls._presence = object.__new__(cls, *args, **kwargs)
                return cls._presence

            def __init__(self):
                config.interact_callbacks.append(self.dp_per_interact)

                self.start = time.time()
                self._old_status = ""

                gallery_message = _("Visiting the Gallery")
                settings_message = _("In the Settings")

                self.screen_messages = {
                    "screenshot_gallery": gallery_message,
                    "gallery": gallery_message,
                    "save": _("Saving a game"),
                    "load": _("Loading a game"),
                    "extras": _("Exploring the Extras"),
                    "main_menu": _("In the Main Menu"),
                    "audio_settings": settings_message,
                    "text_settings": settings_message,
                    "display": settings_message,
                    "keymap": settings_message,
                    "character_preview": _("Learning more about the Characters"),
                    "credits": _("Reading the Credits")
                }

                self._check_recording_function = ("obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe").__contains__
                self.recording = False
                self._lock = threading.Lock()

                self._tracking = True
                self._thread = threading.Thread(target=self.track_recording)
                self._thread.daemon = True
                self._thread.start()

                config.at_exit_callbacks.append(self.stop_track_recording)

                self.init_rpc()

            def init_rpc(self):
                self.set_force_update()
                discord_rpc.initialize("1040341661617762345", callbacks={
                    'ready': self.ready_callback,
                    'disconnected': self.disconnected_callback,
                    'error': self.error_callback,
                }, log=False)
                self.update_info()

                self.force_one_update = False
                renpy.restart_interaction()

            def shutdown(self):
                self.clear_presence()
                discord_rpc.shutdown()
                renpy.restart_interaction()

            def track_recording(self):
                while self._tracking:
                    if renpy.windows:
                        try:
                            process_list = subprocess.run("wmic process get Description", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n")
                        except subprocess.CalledProcessError:
                            try:
                                process_list = (x + ".exe" for x in subprocess.run("powershell (Get-Process).ProcessName", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").strip().split("\n"))
                            except: 
                                process_list = [ ]            
                    else:
                        try:
                            process_list = subprocess.run("ps -A --format cmd", check=True, shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
                        except subprocess.CalledProcessError:
                            process_list = subprocess.run("ps -A -o command", check=True, shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")

                        process_list.pop(0)

                    with self._lock:
                        recording = any(map(self._check_recording_function, process_list))

                        if self.recording is not recording:
                            self.recording = recording
                            renpy.restart_interaction()

            def stop_track_recording(self):
                self._tracking = False
                self._thread.join()

            def dp_per_interact(self):            
                if not persistent.discord_rpc: return

                if self.recording:
                    status = __("Recording...")
                    
                else:
                    for screen_name, message in self.screen_messages.items():
                        if renpy.get_screen(screen_name) is not None:
                            status = __(message)
                            break
                    else:
                        if not store.main_menu:
                            status = __("Playing through Week {week} - {day}").format(week=store.week, day=__(store.day))
                        else:
                            status = "error"

                self.update_presence(status)

            def set_force_update(self):
                self.force_one_update = True

            def update_info(self):
                discord_rpc.update_connection()
                discord_rpc.run_callbacks()
                return

            def update_presence(self, status):
                if self._old_status == status and not self.force_one_update: return

                discord_rpc.update_presence(
                    details=status,
                    start_timestamp=self.start,
                    large_image_key="ddu_logo",
                    small_image_key="studiosilver",
                    large_image_text=__("This game is an unofficial fan game, unaffiliated with Team Salvato."),
                    small_image_text=__("A Studio Silver mod"),
                )
                self.update_info()

                self._old_status = status
                self.force_one_update = False

            def clear_presence(self):
                self.set_force_update()
                self.update_presence("")

            def TurnOn(self):
                return [
                    SetField(persistent, "discord_rpc", True),
                    Function(self.init_rpc)
                ]

            def TurnOff(self):
                return [
                    SetField(persistent, "discord_rpc", False),
                    Function(self.shutdown)
                ]

        dp = DiscordPresence()
    
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
