def bubblesort(arr):
    print("Bubble Sort")
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
        
        print(arr)
        if(flag == False):
            break
    
def shellsort(arr):
    print("Shell Sort")
    n = len(arr)
    gap = int(n//2)
    while(gap>0):
        print(arr)
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j-=gap

            arr[j]=temp

        gap=int(gap//2)
    
    print(arr)


arr=[5,4,3,6,1]
shellsort(arr.copy())
bubblesort(arr.copy())
