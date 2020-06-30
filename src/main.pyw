import os
import subprocess
import atexit
import time
import proc
from pynput import keyboard
from py_macro.macros import MACROS


LUAMACROS_PATH = r''        # input your LuaMacros.exe path here

ON_PRESS_DELAY = 0.5


keypressed_path = os.path.abspath(os.path.dirname(__file__))[:-3] + r'\res\keypressed.txt'
luamacros_script_path = os.path.abspath(os.path.dirname(__file__)) + r'\TaranVH_LUAMACROS\SECOND_KEYBOARD_script_for_LUA_MACROS.lua'


def main():
    # kill LuaMacros process upon exiting
    atexit.register(proc.kill_proc_by_name, 'LuaMacros.exe')

    # set low priority
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


    def on_f20_press(key):
        if key == keyboard.Key.f20:
            keypressed = read_keypressed()
            print(keypressed)
            if keypressed in MACROS.keys():
                MACROS[keypressed].run()
                wipe_keypressed()
            time.sleep(ON_PRESS_DELAY)

    # open LuaMacros script
    subprocess.Popen([LUAMACROS_PATH, '-r', luamacros_script_path])

    # listen for f20
    with keyboard.Listener(on_press=on_f20_press, on_release=None) as listener:
        listener.join()


main()
