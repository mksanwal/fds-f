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

def magicsqaure(m):
    
    if(len(m) == len(m[0])):
        d1 = 0
        d2 = 0
        for i in range(len(m)):
            d1+=m[i][i] 
            d2+=m[i][len(m)-1-i]

        if(d1 == d2):
            for i in range(len(m)):
                r=0
                for j in range(len(m)):
                    r+=m[i][j]
                
                if(r!=d1):
                    return False
                
            for i in range(len(m)):
                c=0
                for j in range(len(m)):
                    c+=m[j][i]
                
                if(c!=d1):
                    return False
                
            
            return True

        else:
            return False

    else:
        return False

# -----------------------------------------------

matrix1=[[2,7,6],[9,5,1],[4,3,8]]
matrix2=[[9,2,7],[4,6,8],[5,10,3]]
if(magicsqaure(matrix2)):
    print("True")
else:
    print("False")


sum_matrix=add(matrix1,matrix2)
for row in sum_matrix:
    print(row)

multiply_matrix=multiply(matrix1,matrix2)
for row in multiply_matrix:
    print(row)