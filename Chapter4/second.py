''' Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:'''

hours = input("Enter hours: ")
rate = input("Enter tax rate: ")
try:
    numh = int(hours)
    numr = int(rate)
    if numh <= 40:
        pay = numh * numr
    else:
        pay = 40 * numr + (numh - 40) * numr * 1.5
    print("Pay:", pay)
except:
    print("Error, please enter numeric input")