while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")