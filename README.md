# Python-2nd-Keyboard-Macros

 
A kinda wonky way to use a 2nd keyboard as a macro keyboard and the *twist* is that I'm using python; therefore knowledge of Python would be helpful
 - [**luamacros**](https://github.com/me2d13/luamacros) **is needed.**
 - **Heavily based on** [**TaranVH's luamacros script**](https://github.com/TaranVH/2nd-keyboard/blob/master/LUAMACROS/SECOND_KEYBOARD_script_for_LUA_MACROS.lua).


## Setup

 1. Download [luamacros](https://github.com/me2d13/luamacros).
 2. Connect the 2nd keyboard and run [/src/TaranVH_LUAMACROS/SECOND_KEYBOARD_script_for_LUA_MACROS.lua](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/src/TaranVH_LUAMACROS/SECOND_KEYBOARD_script_for_LUA_MACROS.lua) in luamacros.
 3. Copy the keyboard's identifier code to the keyboardIdentifier variable. *(Read comments in the script for an explanation)*
 4. Input absolute path to the [/res](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/tree/master/res) folder of the project *(honestly I can't figure out how to put relative path in there)*.
 5. Verify [/res/keypressed.txt](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/res/keypressed.txt) is being written to.
 6. Input your LuaMacros.exe file path to [/src/main.pyw](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/src/main.pyw), LUAMACROS_PATH.
 7. Verify it's run main.pyw and verify it's working. 
 8. Configure your macros in the [**/src/py_macro/macros.py](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/src/py_macro/macros.py) module *(just input your methods with their args/kwargs into the corresponding Macro object in MACROS dict)*.
 9. Input your pythonw.exe path into [/run_macro_keyboard.bat](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/run_macro_keyboard.bat) and pray for the best.

## Files

    /res
	    keypressed.txt		// File storing the current pressed key 
    /src
	    /py_macro
		    __init__.py
		    macro.py		// Module containing the Macro object
		    macros.py		// Module where you set up macros
		/TaranVH_LUAMACROS
			SECOND_KEYBOARD_script_for_LUA_MACROS.lua 		//TaranVH's lua script
		main.pyw			// Module to run
		proc.py				// Module used to optimise it a little bit
	README.MD
	run_macro_keyboard.bat	// Batch file to run
	    

## How it's botched
[**luamacros**](https://github.com/me2d13/luamacros) with [**TaranVH's script**](https://github.com/TaranVH/2nd-keyboard/blob/master/LUAMACROS/SECOND_KEYBOARD_script_for_LUA_MACROS.lua) intercepts the keyboard input, writes the pressed key to [/res/keypressed.txt](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/res/keypressed.txt) *(hopefully)* and virtually presses the F20 key.  Upon "seeing" it pressed, the python script reads from [/res/keypressed.txt](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/res/keypressed.txt) and runs the corresponding Macro object's function (from [/src/py_macro/macros.py](https://github.com/k-xlsx/Python-2nd-Keyboard-Macros/blob/master/src/py_macro/macros.py), MACROS dict).
