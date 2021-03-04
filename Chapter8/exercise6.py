'''Exercise 6: Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0'''

list_number = list()
while True:
    number = input("Enter a number: ")
    try:
        if number == 'done':
            break
        list_number.append(number)
    except:
        print("Invalid input")

max_number = max(list_number)
min_number = min(list_number)
print("Maximum:", max_number)
print("Minimum:", min_number)