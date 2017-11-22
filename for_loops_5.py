# FOR LOOPS:

# in python and every other programming language, if you want to write the same or very similar lines of code one after another
# there's an easier way to do that with for loops
# for loops pretty much repeat their code a certain number of times with the variation of (usually) one variable
# for loops look like this:
my_list = [1, 3, 632, 1]
for i in my_list:
    pass

# the i variable in the for loop can be replaced by any variable name

# in the code of the for loop code, the variable defined at the beginning of the for loop (i in the case above) is
# each element of the list
# for loops pretty much run their code FOR EVERY ELEMENT IN THE ARRAY where the variable defined (i) is the array element
# in the case above the code is run with i as 1 then 3 then 632 and then 1 because those are the elements of the list

# EXAMPLES:
pony_list = ["I", "love", "ponies"]
for pony in pony_list:
    if pony == "I":
        pass
    pass

long_numbers_list = [3, 234, 12, 0, 3, 5, 23, 87, 345, 9, 65]
for jim in long_numbers_list:
    brian = jim*brian
    pass

 # EXERCISES:

 # make 4 for loops that print their variable

 # usually, the lists in for loops are created by the range() function
 # the basic (but not only) way to use the range() function is by giving it one number argument
 # which looks like:
 range(10)
 # this makes a list with all numbers from 0 to 9
 # range used this way pretty much makes a list from 0 to one less than the number argument

 # EXAMPLES:

 numbers_list = range(5) # list from 0 to 4
 pig_numbers = range(3) # list from 0 to 2
 my_list = range() # invalid because range() must have at least one argument
 my_list = range(-5) # just makes an empty list. Negatives can be used in range but not with just one number

 # range is often used to make lists for for loops
 # EXAMPLES:
 for i in range(10):
     pass

 for j in range (5):
     pass

# EXERCISES
# make 2 for loops that use lists made with the range() function which print all of the numbers
# MAKE SURE THE LISTS ARE LESS THAN 100 LONG 
