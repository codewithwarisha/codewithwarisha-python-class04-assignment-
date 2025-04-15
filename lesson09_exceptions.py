# Handling an error
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
