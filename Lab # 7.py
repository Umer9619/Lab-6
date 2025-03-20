num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i  
print("Factorial of", num, "is", factorial)


num = int(input("Enter a number: "))

if num < 2:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:  
        print(num, "is a prime number")
