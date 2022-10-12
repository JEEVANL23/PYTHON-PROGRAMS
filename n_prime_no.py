n = int(input())
print("prime no :" ,end = ' ')
for n in range(0,n+1):
    for i  in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end=' ')    