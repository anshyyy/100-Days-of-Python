def my (a,b):
    if a=="" or b=="":
        return 
    return (f"{a.title()} {b.title()}")

name =input()
surname=input()
print(my(name,surname))
