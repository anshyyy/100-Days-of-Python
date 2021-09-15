def isleap(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return "Leap year"
            else:
                return "not lear year"
        else:
            return "Leap year"
    else:
         return "Not leap year"

def monthday(year,month):
    mon=[31,28,31,30,31,30,31,31,30,31,30,31]
    mon_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    ans=isleap(year)
    if ans=="Leap year":
        return mon_leap[month-1]
    else:
        return mon[month-1]


ye=int(input())
moh=int(input())
print(monthday(ye,moh))
