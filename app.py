your_weight = int(input("Weight: "))
weight_unit = input("(L)bs or (K)gs").upper()
if weight_unit == "L":
    converted_weight = your_weight*0.45
    print(f"You are {converted_weight} kilos")
elif weight_unit == "K":
    converted_weight = your_weight/0.45
    print(f"You are {converted_weight} pounds")
else:
    print("Please enter a real value!")