# Temp converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F)?: ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32, 1) # Convert Celsius to Fahrenheit
    print(f"The temp in Fahrenheit is: {temp}°F")

elif unit == "F":
    temp = round((temp - 32) * 5/9, 1) #Convert Fahrenheit to Celsius
    print(f"The temp in Celsius is: {temp}°C")

else:
    print(f"{unit} is not a valid unit. Please enter C or F.")