#
# Example file for working with conditional statements (if-then, etc.)
#

def main():
    x, y = 10, 100

# Conditional flow uses if, elif, else
    if(x<y):
        st = "x is less than y"
    elif(x==y): # Same as Java's "else-if" condition
        st = "x is the same as y"
    else:
        st = "x is greater than y"
    print(st)

# Conditional statements lets you use "A if C else B" -> This is another format to the if-else conditional configuration
    st = "x is less that y" if(x<y) else "x is greater than or the same as y"
    print(st)

if __name__ == main():
    main()