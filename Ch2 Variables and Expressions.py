#Variables and Expressions

#Declare a variable and initialize it
f=0
# print(f)

#re-declaring the variable works
# f="abc"
# print(f)

#ERROR: Variables of different types cannot be combined
# print("this is a string "+ str(123)) #The str(__) function converts the number '123' to a string

#Global vs. local variables in functions
def someFunction():
    f="def" #This 'f' is inside the function so this is a local variable
    print(f)

someFunction()
print(f)