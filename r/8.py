def partition(arr,left,right):
    i=left
    j=right-1
    pivot = arr[right]

    while(i<j):
        while(i<right and arr[i]<pivot):
            i+=1
        while(j>left and arr[j]>=pivot):
            j-=1

        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    if(arr[i]>pivot):
        arr[i],arr[right]=arr[right],arr[i]

    print(arr)
    
    return i

def quick_sort(arr,low,high):
    if(low<high):
        pivotpostition = partition(arr,low,high)
        quick_sort(arr,low,pivotpostition-1)
        quick_sort(arr,pivotpostition+1,high)

arr=[3,17,4,1,9]
quick_sort(arr,0,4)