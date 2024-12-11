def sentinal_Search(arr,n,key):
    last = arr[n-1]
    arr[n-1] = key
    for i in range(n-1):
        if(arr[i]==key):
            return True
    
    if(last == key):
        return True
    else:
        return False
    
def binary_search(arr,n,key):
    s=0
    e=n-1
    arr.sort()
    while(s<=e):
        mid = (s+e)//2
        if(arr[mid] == key):
            return True
        elif(arr[mid]>key):
            e=mid-1
        elif(arr[mid]<key):
            s=mid+1

    return False
    
arr=[4,5,1,2,3]
key=3

print("______________MENU__________________")
print("Enter 1 for Sentinal Search ")
print("Enter 2 for Binary Search ")
print("Enter 0 to exit")
choice= int(input("Enter choice :"))
while(True):
    if(choice == 1):
        if(sentinal_Search(arr,5,key)):
            print("True")
        else:
            print("False")
    elif(choice == 2):
        if(binary_search(arr.copy(),5,key)):
            print("True")
        else:
            print("False")
    elif(choice == 0):
        print("Bie bie")
        break
    else:
        print("Enter right choice")
    
    print("______________MENU__________________")
    print("Enter 1 for Sentinal Search ")
    print("Enter 2 for Binary Search ")
    print("Enter 0 to exit")
    choice= int(input("Enter choice :"))






