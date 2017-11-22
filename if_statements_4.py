# IF STATEMENTS

# to understand if statements, you first have to understand boolean operators
# boolean operators compare 2 peices of data and output True of False
# the boolean operators are:
# a == b checks if a and b are equal
# a != b checks if a and b are not equal
# a < b checks if a is less than b
# a > b checks if a is greater than b
# a <= b checks if a is less than or equal to b
# a >= b checks if a is greater than or equal to b
# and some other more complicated onces that you'll probably just learn in the future
# EXAMPLES
my_bool = 5 == 5 # valid way to make True boolean because 5 equal 5
a = 10
my_bool = a > 5 # valid way to make True boolean because 10 is greater than 5
my_bool = a < 5 # a valid way to make False boolean because 10 is not less than 5

# EXERCISES:
# make 5 booleans in variables using the boolean operators and make sure the file still runs

# now onto if statements:
# if statements run code if the boolean given to the if statement is True
# they look like:

if True: # note: the boolean can also be False but then the code doesn't run
    pass
    # code
    # code

# if statements can obviously also use things that represent booleans like boolean operators and variables
# EXAMPLES:

if False:
    pass # a valid if statement that doesn't run its code

my_bool = True
if my_bool:
    pass # a valid if statement that runs its code

if 5 == 5:
    pass # a valid if statement that runs its code

if 10 != 45:
    pass # a valid if statement that doesn't run its code

if 8 > 7:
    pass # a valid if statement that doesn't run its code

# EXERCISES:

# make 6 if statements that use boolean operators for the booleans. If you want you can make the code in the if statements print something

# if statements can also have "else" parts that run if the boolean in the if statement is false
# an if statement with an else part looks like:
if 5 == 10:
    pass
else:
    pass # this code runs because the boolean 5 == 10 is false

# the word else should be written at the same indentation level as the if or else your code won't work since python depends on
# indentation to read commands properly

# EXAMPLES:

if True:
    pass
else:
    pass # the code in the else statement runs here

if True:
    pass
    # else:
    #     pass # this is invalid because the indentation level of the else statement isn't the same as the if statement

# else:
#     pass # this is invalid because the else statement isn't directly below an if statement

# EXERCISES:
# make 4 if statements with else statements on each one. Make sure the code of the else statements runs

# in between if and else statements, there can also be an elif statement
# like the if statement, the elif statement takes a boolean
# the elif statement runs if the previous if statement doesn't run OR the previous elif statement doesn't run
# there can be multiple elif statements below one another
# elif statements must be below if statements and above else statements if there is an else statement

# EXAMPLES:
if False:
    pass
elif True:
    pass # the code in the elif statement runs

if 5 == 10:
    pass
elif 5 == 9:
    pass
elif 5 == 6:
    pass
else:
    pass # the code here runs because none of the booleans in the if or elif statements are true

if 6 > 10:
    pass
elif 5 > 2:
    pass # code here runs because boolean is true
elif 10 == 10:
    pass # code here doesn't run because the previous elif statement is true
else:
    pass # code here doesn't run because the previous elif statement is true

# elif 5 == 10:
#     pass # this is invalid because the elif statement is before an if statement
# if 5 == 10:
#     pass
#
# if 5 == 10:
#     pass
# else:
#     pass
# elif: 2 == 2:
#     pass # this is invalid because the elif statement is below an else statement

# EXERCISES:
# make 2 if statements with 3 elif statements and an else statement. Make sure the code in the elif statements runs

# make 5 more if statements with elif statements

# make 3 if statements with 1 elif statement and an else statement
