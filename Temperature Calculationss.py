print("Welcome to Temperature Calculator")
while True:
    print("\n====== Conversion Menu =======")
    print('''1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
3. Exit''')

    user_choice=int(input("Enter your choice: "))
    try:
        if user_choice==3:
            break
        elif user_choice<=0 or user_choice>2:
            print("Invalid Selection, Please try again")
            continue
    
        user_input=float(input("Enter the temperature you want to convert: "))

        if user_choice==1:
            temp_in_celsius= 5/9*(user_input-32)
            print("Temperature in Celsuis is:",temp_in_celsius)
        elif user_choice==2:
            temp_in_fahrenheit= user_input*(9/5)+32
            print("Temperature in Fahrenheit is:",temp_in_fahrenheit)

    except ValueError:
       print("Invaid input! Please enter a valid number.")
    except Exception as e:
       print(f"An error occurred: {e}")
print("Exiting the Calculator. Goodbye!")