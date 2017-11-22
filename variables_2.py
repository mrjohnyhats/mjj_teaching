# VARIABLES

# WHAT IT IS:
# a variable is pretty much a thing that you can use write as a substitute to writing actual data.
# If you define the variable in your code before you use it (in the lines before), python will read the varible as
# the data it represents

# variables are useful if you don't want to write a long piece of data multiple times,
# you want to name a piece of data (ex: naming the number 800 "width" so that the code is easier to read)
# you don't know what the data will be (ex: you're getting data from the internet)
# and many other reasons

# variables are really common in all programming and you pretty much have to know how to use them

# a special property about variables (in most cases) is that they only represent pure data, not other variables.
# In other words, if you have a variable called supreme equal to the number 5 and another variable named fake_supreme
# equal to the variable supreme, then fake_supreme is actually just equal to 5.
# That means that if you add 10 to fake_supreme, supreme stays the same and only fake_supreme changes.
# there are some exceptions to this rule if the piece of data is really big and python doesn't want to copy it, but in
# pretty much every common case it's true

# HOW TO NAME VARIRABLES:
# variables should have descriptive names that represent what they are and what they do
# if you just have random variable names, then your code will be really confusing unless you add tons of comments

# also, in python it is VERY frowned upon to use camelCase (capital letters) to represent different words because
# using snake_case (underscores) is better.
# ex: naming a variables fakeSupreme is bad but naming a variable fake_supreme is good

# variable names also can't have spaces

# SIDENOTE: the concept of writing code so that it can be understood without having to add comments is called "self documenting code"
# and it's a really good rule to follow. You should always make sure that you can understand what your code is doing by reading it.

# HOW TO MAKE VARIABLES:
# making variables is really easy in python.
# To make a variable, write the name of your variable, a space, an equals sign, a space, and your data

# EXAMPLES:
a = 10 # a valid variable
my_variable = a # a valid variable that equals 10
my_list = [1, 2, 3] # a valid variable
myList = [1, 2, 3] # technically a valid but very frowned upon variable
some_bool = True # a valid variable
my_bool = some_bool # a valid variable
s = "some words" # valid variable

# my string = "some words" # an invalid variable because it uses spaces
# "my string" = "some words" # an invalid variable because quotes around words is a string not a variable name


# USING VARIABLES:

# in python variables are interpreted as regular data, so you can just write the variable name instead of the data

# EXAMPLES:
b_emoji = "banned on /r/dankmemes :("

some_list = [b_emoji, "another string"] # a valid way to express the text b_emoji is equal to without actually writing it
some_list = ["b_emoji", "another string"] # an invalid way to express the text b_emoji represents because b_emoji has quotes around it
# which makes python interpret b_emoji as words instead of a variable

# EXERCISES:
# make 10 valid variables using every data type you've learned and make sure the code runs

# make 5 variables equal to other variables and make sure the code runs

# make 3 lists using your variarbles and make sure your code still runs (and you don't put quotes around your varirables)
