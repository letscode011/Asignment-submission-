# Assignment No.4 
# Q.4
# Sachin Dharankar.
# Python program to implement dequeue for queue

f = -1
r = -1
size = 5
l = list()

def enqueue(x):
    global f,r,size,l
    if r == size-1:
        print("Queue full")
        return
    if r == -1:
        f = r = 0
    else:
        r += 1
    l.insert(r ,x)   

def dequeue():
    global f,r,size,l
    if f == -1:
        print("Queue empty")
        return
    x = l[f]
    l.pop(f)    
    if f == r:
        f = r = -1
    else:
        f += 1

def display():
    global f,r,size,l
    if f == -1:
        print("Queue empty")
        return
    for i in range(f-1,r):
        print(l[i], end=" ") 


enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
display()           
