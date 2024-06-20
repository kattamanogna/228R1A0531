'''A=[[1,2],[3,4]]
B=[[1,2],[3,4]]
c=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        c[i][j]=A[i][j]+B[i][j]

for i in c:
    print(i)'''
r=int(input("enter no of rows"))
c=int(input("enter no of columns"))
mat =[]
print("Read matrix")
for i in range(r):
    x=[]
    for j in range(c):
        x.append(int(input()))
    mat.append(x)
print("Matrix is:")
for i in range(r):
    for j in range(c):
        print(mat[i][j],end="  ")
    print()
r1=int(input("enter no of rows"))
c2=int(input("enter no of columns"))
mat1 =[]
print("Read matrix")
for i in range(r1):
    x=[]
    for j in range(c2):
        x.append(int(input()))
    mat.append(x)
print("Matrix is:")
for i in range(r1):
    for j in range(c2):
        print(mat1[i][j],end="  ")
    print()
for i in range(r):
    for i in range(c):
        A[i][j]=()