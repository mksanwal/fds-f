def sentinal_search(arr,key):
    n=len(arr)
    temp = arr[n-1]
    arr[n-1]=key
    for i in range(n):
        if(arr[i]==key):
            ans=i
    arr[n-1]=temp 
    if(ans==n-1 and key!=temp):
        return -1
    
    return ans
    
       

arr = []
n=int(input("total number"))
for i in range(n):
    no=int(input())
    arr.append(no)
key=int(input("YOUr key: "))    
print(sentinal_search(arr,key))    
    


# Sentinel Search:
 
# Sentinel Search is an optimized version of linear search that avoids checking whether the index is within bounds during each iteration.
# Instead, it places the target value (key) at the end of the list (sentinel), which simplifies the loop termination condition.
# After searching, the sentinel value is restored.


# Best case: The key is found at the first index, so the loop will terminate after one comparison. Thus, the time complexity in the best case is 𝑂(1)

# Worst case: The key is either not in the array or it is at the last position. 
# The loop will iterate over all  elements (including the sentinel), resulting in a time complexity of O(n).

# Average case: On average, the key might be found around the middle of the array, so the time complexity will still be O(n).