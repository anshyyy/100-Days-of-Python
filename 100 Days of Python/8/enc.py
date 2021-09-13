c = "a" # character
i = ord(c) # ordinal (ASCII) value of the character
print(i)
# conversion from an ASCII value to text
# i = 98
# c = chr(i)
# print("The ASCII value of %s was converted to its textual value of %d" % (c, i))
c='abc'
msgg=""
for i in range(len(c)):
    x=ord(c[i])
    x+=3
    msgg =msgg+ chr(x)
    
print(msgg)