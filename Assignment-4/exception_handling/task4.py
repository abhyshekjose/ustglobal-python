try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Division:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter only numbers")
else:
    print("Calculation successful")
finally:
    print("Program execution completed")