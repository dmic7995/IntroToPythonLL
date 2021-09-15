#
# Example file for working with loops
#

def main():
    x = 0

# Define a while-loop
#    while (x<5):
#        print(x)
#        x=x+1

# Define a for-loop
#    for x in range(5, 10): #These for-loops are iterators - the range function gives you that range of numbers
#        print(x)

    #This range function is the same as for(i=5, i<10; i++) -> The 'i' count stops at 9
# Use a for-loop over a collection
#    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#    for d in days:
#        print(d)

# Use the break and continue statements
for x in range (5, 10):
    if (x==7): break
    print(x)

 if __name__ == "__main__":
     main()
