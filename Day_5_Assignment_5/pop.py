# Assignment No.4 
# Q.3
# Sachin Dharankar.
# Python program to implement pop on stack

l = list()
top = -1
size = 5

def push(x):
    global top,size,l
    if top == size-1:
        print("Stack is full ")
        return
    top += 1
    l.insert(top,x)

def pop():
    global top,size,l
    if top == -1:
        print("Stack is empty nothing to pop")
        return
    l.pop(top)    
    top = top-1

def display():
    global top,size,l
    if top == -1:
        print("Stack is empty nothing to pop")
        return
    for i in range(top,-1,-1):
        print(l[i])    


push(10)
push(55)
push(20)
pop()
display()        