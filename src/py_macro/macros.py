import keyboard
import subprocess
from py_macro.macro import Macro





def run_program(file_path: str, *args):
    subprocess.Popen([file_path, *args])


def open_folder(folder_path: str):
    run_program('explorer', folder_path)


def open_windows_terminal():
    run_program('wt', 'new-tab')


def run_vscode(*args):
    run_program(r'D:\Program Files FAST\Microsoft VS Code\Code.exe', *args)


def run_python_script(file_path: str):
    run_program('python', file_path)


def open_explorer():
    keyboard.press_and_release("win + e")


def run_taskbar_app(num: str):
    keyboard.press_and_release("win + " + str(num))


def show_desktop():
    keyboard.press_and_release("win + d")



MACROS = {
    "escape": Macro(show_desktop),
    "F1": Macro(),
    "F2": Macro(),
    "F3": Macro(),
    "F4": Macro(),
    "F5": Macro(),
    "F6": Macro(),
    "F7": Macro(),
    "F8": Macro(),
    "F9": Macro(),
    "F10": Macro(),
    "F11": Macro(),
    "F12": Macro(),
    "1": Macro(run_taskbar_app, '1'),
    "2": Macro(run_taskbar_app, '2'),
    "3": Macro(run_taskbar_app, '3'),
    "4": Macro(run_taskbar_app, '4'),
    "5": Macro(run_taskbar_app, '5'),
    "6": Macro(run_taskbar_app, '6'),
    "7": Macro(run_taskbar_app, '7'),
    "8": Macro(run_taskbar_app, '8'),
    "9": Macro(run_taskbar_app, '9'),
    "0": Macro(run_taskbar_app, '0'),
    "q": Macro(),
    "w": Macro(open_folder, r'e:\Wideo'),
    "e": Macro(open_explorer),
    "r": Macro(),
    "t": Macro(),
    "y": Macro(),
    "u": Macro(),
    "i": Macro(),
    "o": Macro(),
    "p": Macro(open_folder, r'e:\Programming'),
    "a": Macro(),
    "s": Macro(),
    "d": Macro(open_folder, r'e:\Dokumenty\Własne Dokumenty'),
    "f": Macro(),
    "g": Macro(),
    "h": Macro(),
    "j": Macro(),
    "k": Macro(),
    "l": Macro(),
    "z": Macro(),
    "x": Macro(),
    "c": Macro(),
    "v": Macro(run_vscode),
    "b": Macro(),
    "n": Macro(),
    "m": Macro(),
    "space": Macro(),
    "tab": Macro(open_windows_terminal),
    "capslock": Macro(),
    "rShift": Macro(),
    "rCtrl": Macro(),
    "backspace": Macro(),
    "enter": Macro(),
    "insert": Macro(),
    "home": Macro(),
    "pageup": Macro(),
    "delete": Macro(),
    "end": Macro(),
    "pagedown": Macro(),
    "`": Macro(run_vscode, __file__),
    "minus": Macro(),
    "equals": Macro(),
    "leftbracket": Macro(),
    "rightbracket": Macro(),
    "singlequote": Macro(),
    "semicolon": Macro(),
    "backslash": Macro(),
    "comma": Macro(),
    "period": Macro(),
    "slash": Macro(),
    "numDiv": Macro(),
    "numMult": Macro(),
    "numMinus": Macro(),
    "numPlus": Macro(),
    "numLock": Macro(),
    "numDelete": Macro(),
    "num0": Macro(),
    "num1": Macro(),
    "num2": Macro(),
    "num3": Macro(),
    "num4": Macro(),
    "num5": Macro(),
    "num6": Macro(),
    "num7": Macro(),
    "num8": Macro(),
    "num9": Macro(),
    "up": Macro(),
    "down": Macro(),
    "left": Macro(),
    "right": Macro(),
}
