import os
import subprocess
import atexit
import time
import proc
from pynput import keyboard
from py_macro.macros import MACROS


LUAMACROS_PATH = r'D:\Program Files FAST\luamacros\LuaMacros.exe'

ON_PRESS_DELAY = 0.5


keypressed_path = os.path.abspath(os.path.dirname(__file__))[:-3] + '/res/keypressed.txt'
luamacros_script_path = os.path.abspath(os.path.dirname(__file__)) + '/TaranVH_LUAMACROS/SECOND_KEYBOARD_script_for_LUA_MACROS.lua'


def main():
    atexit.register(proc.kill_proc_by_name, 'LuaMacros.exe')

    proc.set_low_proc_priority()

    def file_exists(func):
        def wrapper():
            try:
                return func()
            except FileNotFoundError:
                raise FileNotFoundError('keypressed.txt not found in the /res folder')
        return wrapper

    @file_exists
    def read_keypressed() -> str:
        with open(keypressed_path, 'r') as keypressed_file:
            return keypressed_file.readline()

    @file_exists
    def wipe_keypressed():
        with open(keypressed_path, 'w') as _:
            return


    def on_press(key):
        if key == keyboard.Key.f20:
            keypressed = read_keypressed()
            if keypressed in MACROS.keys():
                MACROS[keypressed].run()
                wipe_keypressed()
            time.sleep(ON_PRESS_DELAY)


    subprocess.Popen([LUAMACROS_PATH, '-r', luamacros_script_path])

    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()


main()
