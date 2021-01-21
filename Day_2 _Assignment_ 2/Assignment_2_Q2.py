# Assignment No.2 
# Q.2
# Sachin Dharankar.
# Python program to print a pattern
   
n = int(input("Enter no of rows:"))           #Taking input from user
k = n - 1                                     #Calculating no. of spaces
    # outer loop to handle number of rows
for i in range(1, n+1):
     
        # loop to print spaces (inner loop)
    for j in range(1, k+1):
        print(end=" ")
        # decrementing k after each loop
    k = k - 1
     
        # inner loop to handle number of columns
    for j in range(1, i+1):

        print(i, end="")

    print("\r")
 
