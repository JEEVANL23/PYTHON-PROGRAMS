n1 = 0
n2 = 1
n = int(input())
print(n1)
print(n2)
for i in range(2,n): # starting from 2 bcoz  0 & 1 are already printed 
    sum = n1+n2
    print(sum)
    n1=n2
    n2=sum