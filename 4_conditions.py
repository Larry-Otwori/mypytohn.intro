# python uses 'if' statements to evaluate conditions
# notice that type casting is used here
#drivers_age = int(input("please enter your age: "))
# if (drivers_age >= 18):
#print("Eligible to have driving liscence")
# if code is written here where there is an indent, it will be taken as part of the if statement. so, backspace to go back to edge then write to take code out of if statement
# else:
# print("Not eligible to have drivers liscence")
# note the format of this line
# print(f"Pleae check back with us in {18 - drivers_age} years")


student_mark = int(input("Enter final mark: "))

if (student_mark >= 70):
    print("Pass Grade A")

elif (student_mark >= 60):
    print("Pass grade B")

elif (student_mark >= 50):
    print("Pass grade C")

elif (student_mark >= 40):
    print("Pass grade D")

else:
    print("Fail")
