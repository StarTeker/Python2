n=int(input())
A = []
h=('')
i=0
mas=[int(j) for j in input().split()]
if(n*n==len(mas)):
    while i < len(mas):
        A.append(mas[i:i+n])
        i+=n       
for i in range(0,n-1):
    for j in range(i+1,n):
        if A[i][j]!=A[j][i]:
            h=('False')
            break
if h!=('False'):
    print('Матрица симметрична')
else:
    print('Обычная матрица')
        
print(len(mas))
print(A)
    