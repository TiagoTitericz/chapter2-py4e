# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature.

tcelsius = float(input("Enter temp in Celsius: "))
tfahr = (tcelsius * (9 / 5)) + 32
print("Temp in Fahrenheit:", tfahr)
