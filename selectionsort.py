arr=[]
n=int(input("Enter No. of Elemets in the array::::"))
for i in range(n):
    k=int(input("Enter the numbers::::"))
    arr.append(k)

for i in range(n):#step
    min=i
    for j in range(i,n):
        if arr[j]<arr[min]:
            min=j  
    arr[min],arr[i]=arr[i],arr[min] #a,b=b,a
print(arr)