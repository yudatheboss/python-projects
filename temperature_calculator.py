#python temp calculator

unit = (input("Please enter your unit (F or C): "))
temp = float(input("Please enter the temperature "))

if unit == "F" or unit == "f":
    temp = temp - 32
    temp = temp / 1.8
    unit = "Celsius"
    print(f"Your temp is: {round(temp, 1)} {unit}")
elif unit == "C" or unit == "c":
    temp = temp * 9/5
    temp = temp + 32
    unit ="Fahrenheit"
    print(f"Your temp is: {round(temp, 1)} {unit}")
else:
    print(f"{unit} is not valid.")