def sub(x,y):
    return(x-y)
def add(x, y):
    return(x+y)
def divide(x,y):
    return(x/y)
def multiply(x,y):
    return(x*y)

def main():
    x = int(input("What is the first number:\n"))
    y = int(input("What is the second number:\n"))
    z = int(input("What would you like to do with these numbers? \n 1. Subtraction\n 2. addistion\n 3. multiplication\n 4. divition\n"))
    if(z==1):
        print("\n" + str(sub(x,y)))
        main()
    elif(z==2):
        print("\n" + str(add(x,y)))
        main()
    elif(z==4):
        print("\n" + str(divide(x,y)))
        main()
    else:
        print("\n" + str(multiply(x,y)))
        main()
main()    

