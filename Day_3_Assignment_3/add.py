# Assignment No.3
# Q.1
# Sachin Dharankar.
# Python program to add two nos. using class and object

class addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print("The addition of two numbers is:",a+b)

a = int(input("Enter first value:"))
b = int(input("Enter second value:"))

obj = addition(a,b)
obj.add()