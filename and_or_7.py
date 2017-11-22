# AND, OR, AND NOT

# if you want to use more than one comparison to make a boolean, you can use the operators "and" and "or"
# there's also the "not" operator
# they do this:
# a and b is True if both a and b are True
# a or b is True if either a or b is True
# not a is the opposite boolean of a. If as is True then not a is False and visa versa

# EXAMPLES:
if 5 > 10 or 6 < 100:
    pass # code runs becasue 6 < 100 is True even though 5 > 10 is False

if 5 < 2 or 6 > 100:
    pass # code doesn't run because both booleans are false

if 5 > 10 and 6 < 100:
    pass # code doesn't run because 5 > 10 is False even though 6 < 100 is True

if not 5 > 10:
    pass # code runs because 5 > 10 is False but "not" inverts it to True

# EXERCISES:
# write at least 3 if statements with and, or, and not (must have at least 1 of each) and make sure the code runs
