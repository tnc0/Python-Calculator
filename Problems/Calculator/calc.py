print("press '=' for quit")    
number1 = int(input("number:"))

while True:
    operator = input("operation:")
    if(operator == "+"):
        number2 = int(input("number:"))
        number1 += number2
        print(number1)
    elif(operator == "-"):
        number2 = int(input("number:"))
        number1 -= number2
        print(number1)

    elif(operator == "/"):
        number2 = int(input("number:"))
        number1 /= number2
        print(number1)

    elif(operator == "*"):
        number2 = int(input("number:"))
        number1 *= number2
        print(number1)
    
    elif(operator == "="):
        break
    
    else:
        print("pls press to an operation.")
