# py_macros
**Here you set up your macros.**
## Getting started
It's fairly straightforward, just write a method with your macro actions and put it in the Macro object corresponding with your chosen button. You can input arguments and keyword arguments after it as well.
**Example:**

    [...]
    "q": Macro(),
    "w": Macro(),
    "e": Macro(print, 'why are we here?', 'just to suffer?'),
    "r": Macro(),
    "t": Macro(),
    [...]

 