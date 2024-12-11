# for maximum element
def maximum(arr):
    maxi = arr[0]
    for i in range(len(arr)):
        if(arr[i]>maxi):
            maxi=arr[i]

    return maxi

def countsort(arr,exp):
    count=[0]*(10)
    output=[0]*(len(arr))

#making bucket 
    for i in range(len(arr)):
        count[((arr[i]//exp )%10)]+=1
    
#placing elments in right position
    for i in range(1,10):
        count[i]+=count[i-1]

    i=len(arr)-1
    while(i>=0):
        output[count[(arr[i]//exp)%10]-1] = arr[i]
        count[(arr[i]//exp)%10]-=1
        i-=1

    for i in range(len(arr)):
        arr[i]=output[i]

    print(arr)


def radix_sort(arr):
    m = maximum(arr)

    exp = 1
    while((m/exp) >=1 ):
        countsort(arr,exp)
        exp*=10

arr=[5,42,333,2,1]
radix_sort(arr)
