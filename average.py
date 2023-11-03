#average inputs
#kalen funai
#11/02/2023

numbers = []
while True:
    userInput = input("input an integer or enter q to quit")
    if userInput == 'q':
        break

    number = float(userInput)
    numbers.append(number)


sumNumbers = sum(numbers)
print("The sum of the values input is", sumNumbers)