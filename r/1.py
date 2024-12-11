def max_freq(marks,n):
    freq={}
    for i in range(n):
        if marks[i] in freq:
            freq[marks[i]]=freq[marks[i]]+1
        else:
            freq[marks[i]]=1;

    maxi = -1 
    ans = -1
    for key,value in freq.items():
        if(value > maxi and key != -1):
            ans = key
            maxi = value
        
    return ans
# -----------------------------------------------------------------------------------------------------

n = int(input("Enter no of students :"))
freq = [0]*100
marks=[]
for i in range(0,n):
    x = int(input("Enter marks(-1 for absent and enter from 0 to 100) : "))
    if(x>100 or x<-1):
        while(True):
            print("Enter correct (b/w -1 - 100)")
            x=int(input("Enter marks : "))
            if(x<101 and x>-2):
                break

    marks.append(x)
    freq[x]=freq[x]+1


absent = 0
passed =0
sum=0
maxi = 0
mini = 100
for i in range(n):
    if(marks[i]>maxi):
        maxi = marks[i]

    if(marks[i]<mini and marks[i]!=-1):
        mini = marks[i]

    if(marks[i]==-1):
        absent=absent+1
    
    if(marks[i]!=-1):
        sum=sum+marks[i]
    
    if(marks[i]>28):
        passed = passed + 1


marks.sort()

#------------------------------------------------------------------------------------------------------
print("-----------MENU------------")
print("Enter 1 for Pass students: ")
print("Enter 2 for Failed students :")
print("Enter 3 for Absent Students :")
print("Enter 4 for Average Marks : ")
print("Enter 5 for Highest Marks : ")
print("Enter 6 for Lowest Marks :")
print("Enter 7 for Maximum Freq :")
print("Enter 8 for Top 3 scorers :")
print("Enter 0 to Exit ")
choice = int(input("Enter Choice : "))
while(choice!=0):
    if(choice == 1):
        print("Passed Students are : ", passed)
    elif(choice == 2):
        print("Failed Students are : ", n-passed)
    elif(choice == 3):
        print("Absent students are : ", absent)
    elif(choice == 4):
        print("average marks are : ", sum/(n))
    elif(choice == 5):
        print("Highest marks are : ",maxi)
    elif(choice == 6):
        print("Lowest marks are : ", mini)
    elif(choice == 7):
        print("Maximum frequency of numbers are : ", max_freq(marks,n))
    elif(choice == 8):
        print("Top scorer :", marks[n-1])
        print("Second Top scorer :",marks[n-2])
        print("Third Top scorer :",marks[n-3])
    elif(choice == 0):
        print("THANK YOU :)")
        break
    else:
        print("Enter write choice :")
    
    print("-----------MENU------------")
    print("Enter 1 for Pass students: ")
    print("Enter 2 for Failed students :")
    print("Enter 3 for Absent Students :")
    print("Enter 4 for Average Marks : ")
    print("Enter 5 for Highest Marks : ")
    print("Enter 6 for Lowest Marks :")
    print("Enter 7 for Maximum Freq :")
    print("Enter 8 for Top 3 scorers :")
    print("Enter 0 to Exit ")
    choice = int(input("Enter choice :"))

print()
print("Give full marks to us")

# -1
# 14
# 14
# 16
# 15