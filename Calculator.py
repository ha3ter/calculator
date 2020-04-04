print("######################################################")
print("#              _            _       _                #")
print("#     ___ __ _| | ___ _   _| | __ _| |_ ___  _ __    #")
print("#    / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|   #")
print("#   | (_| (_| | | (__| |_| | | (_| | || (_) | |      #")
print("#    \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|      #")
print("#                                                    #")
print("#                                   Coded by @Ha3ter #")
print("######################################################\n")


def snap():
    nl = input(" \nSquare root [y]  &  Other operators Like{+ - * / **} [n] : ")
    if nl == 'y':
        number = input("\nEnter your number for the square root : ")
        number = float(number)
        accuracy = 0.001
        guess = (number / 2)

        while abs(number - guess ** 2) > accuracy:
            divide = (number / guess)
            guess = (divide + guess) / 2
        print(" \nYour Number is -> ", number, " And Square Root -> : ", guess)

    elif nl == 'n':

        number_one = float(input(" \nEnter your first number : "))
        char = input("\nEnter your operator [ + , - , * , / , ** ] : ‌")
        number_two = float(input("\nEnter your second number : "))

        if char == "+":
            print('\nSum 2 Numbers :', number_one + number_two)
        elif char == "-":
            print('\nSubtract 2 Numbers :', number_one - number_two)
        elif char == "*":
            print('\nMultiplication 2 Numbers :', number_one * number_two)
        elif char == "/":
            print('\nDivide 2 Numbers :', number_one / number_two)
        elif char == "**":
            print('\nExponentiation 2 Numbers :', number_one ** number_two)
        else:
            print("\nYou entered the operator incorrectly")


ret = input(" Enter your name to run the program : ")
if 1 == 1:
    print("\nHello ", ret, " Welcome :D\n")
    snap()

star = input(" \nStart the program again [y]  &  End of program [n] : ")

if star == "y":
    snap()
else:
    print("\nGOOD LUCK :D")
    exit()