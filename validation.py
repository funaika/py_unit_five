

while True:
        userInput = input("enter a number 1-10")
        if 1 <= int(userInput) <= 10:
            print(userInput)
            break
        else:
            print("invalid input")
