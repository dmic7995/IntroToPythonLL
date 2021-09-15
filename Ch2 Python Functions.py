#
# Example file for working with functions
# 

# define a basic function
def func1():
    print("I am a function")

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# Function that returns a value
def cube(x):
    return(x*x*x)

# Function with a default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num;
    return result

# Function with variable number of arguments
def multi_add(*args): #Keep in mind this always has to be the last parameter
    result=0
    for x in args:
        result = result+x
    return result

# func1()
# print(func1()) #Output is the same as in the first case
# print(func1) #Function itself isnt being executed at all - we are prnting the value of the function definition itself
# func2(10, 20)
# print(func2(10,20))
# print(cube(3))
# print(power(2)) # x is going to default to 1 here
# print(power(2,3)) # x gets overwritten to the value provided here when power() is called
# print(power(x=3, num=2)) # Python lets you call functions with their named parameters along with their values without any particular order
print(multi_add(10, 4, 5, 10, 4))