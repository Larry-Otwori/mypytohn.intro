# python impiments loop using the 'for' keyword
# accompanied by some additional logic

# this is a list. this is how a list is implemeted in python
my_fruits = ["Mango", "Orange", "Peach", "Apple"]
for fruit in my_fruits:  # this is the for loop that will loop through my_fruits list. note that an iterator called 'fruit' has been created to alow traversing of the whole list
    print(fruit)
    # note that '.len' after the list 'my_fruits' is used to get the length of the list
# be very keen on the indentation.
print(f"The list {my_fruits} has {len(my_fruits)} items")

my_name = "Jonathan"
for i in my_name:  # note that here the iterater is i
    print(i)
