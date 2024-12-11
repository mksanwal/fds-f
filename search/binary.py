# Function to perform binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid  # Return index of found key
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if key not found


n = int(input("Enter the number of students: ")) # x = int(input())
arr = []

for i in range(n):
    roll_no = int(input("ENTER ROLL NO : "))
    arr.append(roll_no)

key = int(input("find key"))

print(binary_search(arr , key))





# binary_search(): O(log n)
# input_sorted_roll_numbers(): O(n)
# Overall time complexity: O(n)