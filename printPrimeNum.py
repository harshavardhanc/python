num1 = int(input("Enter the starting number range: "))
num2 = int(input("Enter the ending number range: "))

def checkPrime(num1, num2):
    for i in range(num1, num2):
        if num1 <= 1:
           print("num1 should be greater than 1")
           break
        elif (i % 2) != 0:
           print(i)
           
checkPrime(num1, num2)