fact = 1
n = int(input())
if n<0:
    print("factorial does not exist for negative numbers")
elif n == 0:
    print("factorial of 0 is 1 ")
else:
    for i in range(1,n+1): # total number or if n is there it will count upto n-1 number
        fact*=i
    print(fact)    
