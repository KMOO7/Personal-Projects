print("Welcome to Calculator Software")

while True:
    print("\n====== Calculator Menu ======")
    print('''Select your operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit''')
    try:
        user_choice = int(input("Enter your operation: "))
        if user_choice == 5:
            break
        elif user_choice not in range(1, 5):
            print("Invalid Selection!!, Please try again")
            continue

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if user_choice == 1:
            print("Result:", a + b)
        elif user_choice == 2:
            print("Result:", a - b)
        elif user_choice == 3:
            print("Result:", a * b)
        elif user_choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero! Please try again.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Exiting the Calculator. Goodbye!")

