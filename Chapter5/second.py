'''Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.'''

max_number = None
min_number = None
while True:
    number = input("Enter a number: ")
    try:
        if number == 'done':
            print('The largest number is', max_number)
            print('The smallest number is', min_number)
            break
        else:
            numb = int(number)
            if  max_number == None and min_number == None:
                max_number = numb
                min_number = numb
            elif numb > max_number:
                max_number = numb
            elif  numb < min_number:
                min_number = numb
    except:
        print("Invalid input")