a=[]
dn=[]
n=int(input("Enter length of Array : "))
print("Enter array : ")
for i in range(n):
     x=int(input())
     a.insert(i,x)
     i=i+1
i=0
k=0
while i<n:
    j=i+1
    while j<n:
        if a[i]==a[j]:
           print("First Duplicate Number = ",a[i])
           k=1
           break
        j=j+1
    if k==1:
        break
    i=i+1
