def selection_sort(arr):
    print("_________Selection Sort____________")
    for i in range(len(arr)):
        minm=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minm]):
                minm=j
        
        arr[minm],arr[i]=arr[i],arr[minm]
        print(arr)


def insertion_sort(arr):
    print("______________insertion_sort__________")
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)

    



arr=[5,4,3,2,1]
print("_________MENU___________")
print("Enter 1 for Selection Sort")
print("Enter 2 for Insertion Sort")
print("Enter 0 for exit")
choice = int(input("Enter Choice : "))
while(True):
    if(choice == 1):
        selection_sort(arr.copy())
    elif(choice == 2):
        insertion_sort(arr.copy())
    elif(choice == 0):
        print("Bie bie")
        break
    else:
        print("Enter correct number")
        
    print("_________MENU___________")
    print("Enter 1 for Selection Sort")
    print("Enter 2 for Insertion Sort")
    print("Enter 0 for exit")
    choice = int(input("Enter Choice : "))
        
