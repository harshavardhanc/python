num = int(input("Enter the number: "))



def fact(num):
    if num < 0:
        print("Factorial is not defined for negative integers")
    elif num == 0:
        print("Factorial for %i is 1" %num)
    else:
        factorial = 1
        for i in range(1,num+1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

fact(num)