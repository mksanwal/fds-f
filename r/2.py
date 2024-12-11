# ---------------Functions
def bad_cric_both(cricket,badminton):
    both=[]
    for stu in cricket:
        if stu in badminton:
            both.append(stu)

    print(both)

def bad_or_cric_not_both(total,cricket,badminton):
    not_both=[]
    for stu in total:
        if((stu in cricket and stu not in badminton) or (stu in badminton and stu not in cricket)):
            not_both.append(stu)

    print(not_both)

def no_bad_no_cric(total,cricket,badminton):
    not_both=[]
    for stu in total:
        if((stu not in badminton and stu not in cricket)):
            not_both.append(stu)

    print(not_both)

def cric_foot_no_bad(total,cricket,football,badminton):
    ans=[]
    for stu in total:
        if((stu not in badminton and stu in cricket and stu in football)):
            ans.append(stu)

    print(ans)

def no_game(total,cricket,football,badminton):
    ans=[]
    for stu in total:
        if((stu not in badminton and stu not in cricket and stu not in football)):
            ans.append(stu)

    print(ans)

def least_one(total,cricket,football,badminton):
    ans=[]
    for player in cricket:
        if player not in ans:
            ans.append(player)

    for player in badminton:
        if player not in ans:
            ans.append(player)

    for player in football:
        if player not in ans:
            ans.append(player)
    
    print(ans)

def all_game(total,cricket,football,badminton):
    ans=[]
    for stu in total:
        if((stu in badminton and stu in cricket and stu in football)):
            ans.append(stu)

    print(ans)


#----------------Inputs
cricket=[]
for i in range(5):
    x=int(input("Enter : "))
    cricket.append(x)

football=[]
for i in range(5):
    x=int(input("Enter : "))
    football.append(x)

badminton=[]
for i in range(5):
    x=int(input("Enter : "))
    badminton.append(x)

total=[]
for player in cricket:
    if player not in total:
        total.append(player)

for player in badminton:
    if player not in total:
        total.append(player)

for player in football:
    if player not in total:
        total.append(player)

total.append(69)


print("total : " , end="")
print(total)
print("cricket : " , end="")
print(cricket)
print("football : " , end="")
print(football)
print("badminton : " , end="")
print(badminton)



#----------------Menu
bad_cric_both(cricket,badminton)
bad_or_cric_not_both(total,cricket,badminton)
no_bad_no_cric(total,cricket,badminton)
cric_foot_no_bad(total,cricket,football,badminton)
no_game(total,cricket,football,badminton)
least_one(total,cricket,football,badminton)
all_game(total,cricket,football,badminton)

# 1
# 2
# 3
# 4
# 5
# 6
# 5
# 4
# 3
# 2
# 9
# 7
# 5
# 3
# 1