# arr = [2*n for n in range(1,11) if n%2 == 0]
# print(arr)
#
# names = ['anshyy', 'jay','ray', 'alex']
# new_name = [name.title() for name in names if len(name)>3]
# print(new_name)

# numbers = [1,1,2,3,5,8,13,21,34,55]
# nums= [n for n in numbers if n %2==0]
# print(nums)
arr=[]
arr1=[]
with open('file1.txt') as f1:
     arr = f1.readlines()

arr = [int(i.replace("\n", "")) for i in arr]
print(arr)
with open('file2.txt') as f2:
    arr1 = f2.readlines()

arr1 = [int(i.replace('\n', "")) for i in arr1]
print(arr1)

new_list = [n for n in arr if n in arr1]
print(new_list)
