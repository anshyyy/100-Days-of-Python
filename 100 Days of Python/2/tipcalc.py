print("Welcome to tip calculator.")
b = input("What was the total bill? $")
bill = float(b)
print("what percentage tip would you like to give? 10 ,12 or 15?")
tip= int(input())
bill1 = bill+(bill * (tip/100))
print("how many people to split the bill?")
peo = int(input())
money= bill1/peo
print(f"you have to give ${money}")

