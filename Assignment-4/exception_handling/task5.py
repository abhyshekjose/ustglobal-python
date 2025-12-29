def handle_exceptions():
    try:
        
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")

    except ValueError:
        
        print("Error: Please enter valid integers only.")

    except ZeroDivisionError:
        
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")


handle_exceptions()
