# FUNCTIONS

# functions can technically be considered a data type, but they're much more than that and a really important
# part of python.

# a function pretty much lets you define a block of code under a name that you can use later
# it pretty much says "if I write this function name, then run the code under the function name"
# this looks like:

def my_function():
    # code
    # code
    pass

my_function()

# all functions start with the word def, a space, and then the function name
# then there's some parenthesis for arguments and a colon
# you can obviously write pretty much anything in the block of code (even call the function created, but
# that's not a good idea)

# using the function is called "calling" a function and is done by writing the name of the function with parenthesis and
# the appropriate arguments inside them if any
# if the function doesn't have arguments then you still need to have parenthesis. They just need to be blank

# but what are arguments?
# glad you asked
# arguments are pretty much special variables that you can make for your function to use but aren't actually defined until
# the function is called
# for example, I can have a function called sum(a, b) that takes the arguments a and b
# the function sum(a, b) doesn't know what a and b are, but it knows to output (we'll talk about what output is later) a + b

# when the function sum(a, b) is called, 2 number arguments are given to it that define a and b
# if sum(5, 10) is called, then a is defined as 5 in this case and b is defined as 10
# this will give us an output of 15
# this is the sum function:

def sum(a, b):
    return a + b

my_sum = sum(5, 10)

# but what is this return thing?
# a return statement pretty much makes the function end with an output
# what that means is that when the function ends on return, then it can pretty much be considered a variable that equals the
# return statement
# for example, the sum function above can be seen as 15 because it returned a + b which was the same as 5 + 10 when I called it
# with the arguments 5 and 10
# when return is run in a function, the function also ends completely and the rest of the code in the function doesn't run

# EXAMPLES:

def foo():
    pass
    pass
    return # the function's code below doesn't run because it already returned
    import sys
    sys.exit()

def bar(a):
    return a*10

n = bar(5) # n is equal to 50

def gab(n):
    if n == 10:
        return 5
    return n

a = gab(10) # equals 5
b = gab(1034) # equals 1034

def retarded_function():
    for i in range(1000):
        return i

a = retarded_function() # equals 0 because once the function returns in the for loop, the for loop doesn't run

# EXERCISES:
# make 3 functions that use either an if statement and or for loop (you must have at least one of each)
# these functions also have to return something
# call each of your functions

# make 3 functions that use either an if statement or for loop (you must have at least one of each) that take and use arguments
# the functions have to return something that involves the arguments
# call each function in variable definition (like in the examples above)
