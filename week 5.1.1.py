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
