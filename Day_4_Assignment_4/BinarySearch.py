# Assignment No.4
# Q.2
# Sachin Dharankar.
# Binary search

def binary_search(arr, low, high, x): 
  
    if high >= low: 
  
        mid = (high + low) // 2
  
        # middle Condition 
        if arr[mid] == x: 
            return mid 
  
        # Element smaller than mid
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Element higher than mid 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1

arr = [ 5,10,12,15,55,60 ] 
x = 55

result = binary_search(arr,0,len(arr)-1,x)  

if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
