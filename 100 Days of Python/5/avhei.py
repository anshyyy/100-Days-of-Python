n=int(input("Enter the number of Student\n"))
arr=[]
for i in range(0,n):
    e=int(input())
    arr.append(e)
average=0
for i in range(0,n):
    average+=arr[i]

print(round(average/n))

