# CODE BLOCKS

# in python, when you write code that belongs to an if, for loop, or another thing that takes code, then that code
# is called a block
# a block looks like
if True:
    pass
    pass
    # other code that isn't pass
    pass
    pass

# all of those pass statements and the comment are part of the if statement's block of code
# notice how all of the code in the block doesn't vary in indentation
# there also be blocks of code inside of other blocks of code

# a block of code ends when there is a line of code that is not indented as far as the block of code

# EXAMPLES:

if 5 == 5:
    pass
    pass
    for i in [1, 5, 342]:
        pass # this is a block of code inside a block of code
        pass
    pass # this ends the for loop's block of code and goes back to the if statement

if 5 == 5:
    pass
    pass
pass # this ends the block of code
    pass # this is invalid because it's not indented above an if statement, for loop, or anything else that takes a block of code
# it can't be part of the if statement above becasue that block of code ended with the unindented "pass" statement

def foo():
    pass
    pass
    pass # a valid block of code

# TAKEAWAY: make sure you have good indentation in your code. It's really important in general but especially in python because
# if you don't then your code doesn't run
