while True:
    try:
        n = int(input("Enter a number: "))
        print(n/2)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        
    except:
        print("An unexpected error occurred. Please try again.")