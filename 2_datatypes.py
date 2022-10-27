#Datatypes in python

# primitive datatypes
from operator import truediv


x = 5  # int data type
y = 2.5  # float data type

# declare variables on the same line
#x,y = 5, 2.5

# python allows for the assigning of same value to multiple variables
a = b = c = 3

my_string = {"Hello There"}  # str data type
is_true = True  # Boolean data type
is_false = False  # Boolean data type
my_first_list = [1, 2, 3]  # List data type
none_type = None
# single quotation marks can also be used (inside curly braces)
my_string = {'Hello There'}
my_char = {'a'}

# check for the data types of the variables
print(type(x))
print(type(y))
print(type(a))
print(type(my_string))
print(type(is_true))
print(type(my_first_list))
print(type(none_type))
print(type(my_char))  # take note of this in terms of output

#my_string = {'Hello There'}

read_list = list["berry", "cherry", "mary"]
print(read_list)
