while True:
    print("\n1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")

    option = int(input("Choose an option: "))

    if option == 5:
        print("Exiting calculator. Goodbye!")
        break

    if option in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2
        elif option == 3:
            result = num1 * num2
        elif option == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero")
                continue

        print("Result:", result)
    else:
        print("Invalid option. Try again.")
