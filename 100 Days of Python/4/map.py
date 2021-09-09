r1=["0","0","0"]
r2=["0","0","0"]
r3=["0","0","0"]
map=[r1,r2,r3]
row=int(input("Enter row number"))
col=int(input("Enter coloumn"))
# co=map[row-1]
# co[col-1]="X"
map[row-1][col-1]="X"
print(map)