a=[2,5,6,8,5,7]

max=a[0]
n = len(a)
for i in range(1,n):
    if a[i]>max:        # use < to find min value
        max=a[i]
print(max)         