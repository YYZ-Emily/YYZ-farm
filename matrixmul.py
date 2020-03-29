n=int(input('Enter the number of raws:'))
print('Enter matrix a:')
a=[]
for i in range(0,n):
    a.append(int(x) for x in input().split())
print('Enter matrix b:')
b=[]
for i in range(0,n):
    b.append(int(x) for x in input().split())
c=[]
c.append(a[i][j]*b[i][j] for i in range(n) for j in range(n))
print(c)
print('-'*20)
for i in range(0,n*n):
    for j in range(0,n):
        print(c[i],end=' ')
        print()

