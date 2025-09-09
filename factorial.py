'''num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("Factorial of numbers less than 0 does not exist")
if num == 0:
    print("Factorial of 0 is", 1)
if num > 0:
    for i in range(1, num+1):
        fact= fact*i
    print("The factorial of", num , "is", fact)'''

#Using Recursion
num = int(input("Enter the number: "))

def fact(a):
    if a == 0:
        return 1
    else:
        return (a*(fact(a-1)))
result= fact(num)
print("The factorial of the number is", result)