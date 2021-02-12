'''Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called 
computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0'''

def computepay(hour, rate):
    try:
        numh = int(hour)
        numr = int(rate)
        if numh <= 40:
            pay = numh * numr
        else:
            pay = 40 * numr + (numh - 40) * numr * 1.5
        print("Pay:", pay)
    except:
        print("Error, please enter numeric input")

hours = input("Enter hours: ")
rate = input("Enter tax rate: ")

computepay(hours, rate)
