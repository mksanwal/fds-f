def take_input(n,m):
    matrix=[]
    for i in range(n):
        m=[]
        for j in range(m):
            x=int(input("Val : "))
            m.append(x)
        matrix.append(m)

def add(m1,m2):
    a1=len(m1)
    b1=len(m1[0])
    a2=len(m2)
    b2=len(m2[0])

    if(a1==a2 and b1==b2):
        matrix=[]
        for i in range(a1):
            m=[]
            for j in range(b1):
                x=m1[i][i]+m2[i][j]
                m.append(x)
            matrix.append(m)

        return matrix
    else:
        print("Addition not possible")

def multiply(m1,m2):
    a1=len(m1)
    a2=len(m2[0])
    matrix=[]
    for i in range(a1):
        list = []
        for j in range(a2):
            list.append(0)
        matrix.append(list)

    if(len(m1[0]) == len(m2)):
        for i in range(a1):
            for j in range(len(m1[0])):
                for k in range(len(m2)):
                    matrix[i][j] += m1[i][k]*m2[k][j] 

        return matrix
    else:
        print("Multiplication not possible")

def transpose(m1):
    matrix = []
    for i in range(len(m1[0])):
        m=[]
        for j in range(len(m1)):
            m.append(m1[j][i])
        matrix.append(m)

    return matrix

def saddle_point(m1):
    list=[]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            val=m1[i][j]
            flag = True
            for k in range(len(m1[i])):
                if(val>m1[i][k]):
                    flag = False
                    break
            
            if(flag==False):
                break

            for k in range(len(m1)):
                if(val<m1[k][j]):
                    flag=False
                    break
            
            if(flag == False):
                break
            
            t1 = i
            t2 = j
            temp=[]
            temp.append(t1)
            temp.append(t2)
            temp.append(val)
            list.append(temp)

    return list

# -----------------------------------------------

matrix1=[[2,7,6],[9,5,1],[4,3,8]]
matrix2=[[9,2,7],[4,6,8],[5,10,3]]
matrix3=[[1,2,3],[4,5,6],[7,8,9]]

sum_matrix=add(matrix1,matrix2)
for row in sum_matrix:
    print(row)

multiply_matrix=multiply(matrix1,matrix2)
for row in multiply_matrix:
    print(row)

print("Transpose")
transposed_matrix = transpose(matrix1)
for row in transposed_matrix:
    print(row)

print("saddle")
saddle_p = saddle_point(matrix3)
for i,j,v in saddle_p:
    print(i," ",j," val",v)