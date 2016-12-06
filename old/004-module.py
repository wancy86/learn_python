print("----------------Module----------------")

# 1.
# This does not enter the names of the functions defined in fibo directly in the current symbol table; 
# it only enters the module name fibo there. Using the module name you can access the functions:
import fibo
fibo.fib(100)
fib3=fibo.fib
fib3(100)

# 2.
# This does not introduce the module name from which the imports are taken in the local symbol table (so in the example, fibo is not defined).
from fibo import fib, fib2
fib(500)

# 3.
# this is not recommended, that is frown upon(眉头一皱不赞同，LOL)
# This imports all names except those beginning with an underscore (_).
from fibo import *
fib(100)

# Note: Note For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).

 # The Module Search Path
 # When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.
print('The Module Search Path--------------------')

# not work????
# These two variables are only defined if the interpreter is in interactive mode.
'''
# 命令行开始符
import sys
sys.ps1
sys.ps2
sys.ps1 = 'C> '
print('Yuck!')
'''

print('package--------------------')
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# From the surround module for example, you might use:
'''
from . import echo
from .. import formats
from ..filters import equalizer
'''
# Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.

