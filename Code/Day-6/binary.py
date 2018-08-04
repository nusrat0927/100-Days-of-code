a=[]
n=int(input("Enter a length of arrary : "))

print("Enter array : ")
for i in range(n):
     x=int(input())
     a.insert(i,x)
     i=i+1
i=0
j=n-1
while i<j:
    if a[i]==1 and a[j]==0:
        s=a[i]
        a[i]=a[j]
        a[j]=s
    if a[i]==0:
        i=i+1
    if a[j]==1:
        j=j-1
for i in range(0,n):
    print(" ",a[i])
