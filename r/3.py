def partition(arr, low, high):
    pivot = arr[low]
    i = low+1
    j = high
    
    while(True):
        while(i<=j and arr[i]<=pivot):
            i+=1
        
        while(i<=j and arr[j]>=pivot):
            j-=1
        
        if(i>j):
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]

        print(arr)
        print()
        
        
    arr[low], arr[j] = arr[j], arr[low]
    print(arr)
    print()
    print(j)
    return j


def quick_sort(arr, low, high):
    if(high>low):
        print(arr)
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
 
        
n = int(input("Enter the size of the array : "))
arr = []
for i in range(0, n):
    k = int(input())
    arr.append(k)
n = len(arr)
print()

print("The Unsorted Array is:")
print(arr)
print()

print("The array after each iteration is:")
quick_sort(arr, 0, n-1)
print()

print("The Sorted Array is:")
print(arr)

# 9
# 27
# 76
# 17
# 9
# 57
# 90
# 45
# 100
# 79