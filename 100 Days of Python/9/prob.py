
travel_log=[
    {
        "country":"france",
        "visits":12,
        "cities":["paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["berlin","hamburg","Stuttgart"]
    },
]

def add (a,b,c):
    dict= {}
    dict["country"]=a
    dict["visits"]=b
    dict["cities"]=c
    travel_log.append(dict)

add("russia",2,["Moscow","Saint petersburg"])
print(travel_log)
     