#input in python
# input function allows us to input data and store it in a variable.
# python uses the function input() to capture and store inputin the application
# underscore notation is used for compound variable(according to my understanding varibles with two words e.g first_name)
print("User Profile Application")
print("please enter your first name")
first_name = input("First name:")
print("please enter your last name")
last_name = input("Last Name:")
print("please enter your occupatioin")
occupation = input("Your Job:")


#print("Your first name is " + first_name)
#print("Your last name is " + last_name)
#print("Your occupation is " + occupation)

# python allows you to condense your print statements thats why lines 14-16 are commented out(below)
# another way of outputing info in python is through what's below which is code for comment above
print(f"Your first name is {first_name} and your job is {occupation}")


# handling non-string input
#age = input("please enter your age:")
# print(f"in two years yor age will be {age+2} ") #when run like this, shows error because you can concantenate string with string but not string with int.

# correction for above code. This is called type casting at the point of input
age = int(input("please enter your age:"))
print(f"in two years yor age will be {age+2} ")
