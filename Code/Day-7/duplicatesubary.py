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
           dn.insert(k,a[i])
           k=k+1
           break
        j=j+1
    i=i+1
print("Duplicate subarray : ")
for i in range(0,k):
    print(" ",dn[i])
