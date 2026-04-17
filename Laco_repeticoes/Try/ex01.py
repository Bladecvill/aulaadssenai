while True:
    try:
        number = int(input("Enter a number: "))
        print(number/1)
        break
    except:
        print("Invalid input. Please enter a valid number.")