num = int(input("Enter the number: "))

if num < 1:
    print("Number should be greater than 1")
elif (num % 2) == 0:
    print("%i is not a prime number" %num)
else:
    print("%i is a prime number" %num)