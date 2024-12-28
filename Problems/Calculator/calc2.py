
print("< Basic Calculator >\n"
"Summation: '-' or 'sum'\n"
"Subtraction: '-' or 'subtract'\n"
"Multiplication: '*' or 'multiply'\n"
"Division: '/' or 'divide'\n"
"Exit: '=' or 'exit'\n")

number = int(input('Number to be processed: '))

while True:
    Operation = input('Operation: ')
    if (Operation == '+' or Operation.lower() == 'sum'):
        new_number = float(input('Number to be processed: '))
        number += new_number
    elif (Operation == '-' or Operation.lower() == 'subtract'):
        new_number = float(input('Number to be processed: '))
        number -= new_number
    elif (Operation == '*' or Operation.lower() == 'multiply'):
        new_number = float(input('Number to be processed: '))
        number *= new_number
    elif (Operation == '/' or Operation.lower() == 'divide'):
        new_number = float(input('Number to be processed: '))
        number /= new_number
    elif (Operation == '=' or Operation.lower() == 'exit'):
        print('= %g\n' % number)
        break
    else:
        print('Input is incorrect.\n')
    print('= %g\n' % number)

print("< Basic Calculator >\n")