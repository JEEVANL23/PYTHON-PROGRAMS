# using temp variable


a=[12,34,56,78,90]

size=len(a)

temp=a[0]
a[0]=a[size-1]
a[size-1]=temp
print(a)

