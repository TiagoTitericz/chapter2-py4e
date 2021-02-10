# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = int(input("Enter hours: "))
rate = float(input("Enter tax rate: "))
pay = hours * rate
print("Pay:", pay)