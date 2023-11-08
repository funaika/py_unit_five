def sequence(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        print(1)

inputNumber = int(input("input a number"))
sequence(inputNumber)