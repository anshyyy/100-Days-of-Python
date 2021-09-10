

arr=[]
n=int(input("Enter the number stdents\n"))
for i in range(0,n):
    e=int(input())
    arr.append(e)

maxi=arr[0]
print(arr)
for i in range(1,n):
    if arr[i]>maxi:
        maxi=arr[i]

print(f"maximum element : {maxi}")
