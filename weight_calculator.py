#python weight calculator

weight = float(input("Please enter your weight "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit ="Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid.")