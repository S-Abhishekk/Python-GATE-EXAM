#Using temp variable
'''x = int(input("Enter value of x:"))
y = int(input("Enter value of y:"))
temp = x
print("Value of temp variable:", temp)
x = y
print("Value of x", x)
y = temp
print("Value of y", y)
'''

#Using left and right
x = int(input("Enter value of x:"))
y = int(input("Enter value of y:"))

x,y = y,x
print("Value of x", x)
print("Value of y", y)
