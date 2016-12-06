# Fibonacci numbers module

# They are executed only the first time the module name is encountered in an import statement. 
# [1] (They are also run if the file is executed as a script.)
# he code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:
# all ways run this
print('1. fibo module init statement, by imported/script.......')

# only run when call as script
# If the module is imported, the code is not run:
if __name__ == "__main__":
    print('2. fibo module run as script...........+1')


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# use the defined function, so need be at the bottom
# only run when call as script
# If the module is imported, the code is not run:
if __name__ == "__main__":
    print('2. fibo module run as script...........+2')
    import sys
    fib(int(sys.argv[1])) #get the commond line parameter
    print('2. fibo module run as script...........+2')

