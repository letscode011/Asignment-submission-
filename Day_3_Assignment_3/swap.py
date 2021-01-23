# Assignment No.3
# Q.2
# Sachin Dharankar.
# Python program to swap two numbers.

def swap(a,b):
    temp = a
    a = b 
    b = temp
    print("The value of a after swapping is :",a)
    print("The value of b after swapping is :",b)


a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
swap(a,b)
