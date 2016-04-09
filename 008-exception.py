print("----------------Exceptions----------------")
# 1
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# 2
import sys
try:
    f = open('testfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# 3
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 4
try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)

# 5
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 6  
# Raising Exceptions
raise NameError('HiThere')

# 7 can handle and re-raise exception to outer layer
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# User-defined Exceptions
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

raise MyError('oops!')

# 8
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
with open("testfile.txt") as f:
    for line in f:
        print(line, end="")

        