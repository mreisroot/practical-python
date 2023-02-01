# Function that returns the sum of two numbers
def add_2_numbers(x, y):
    return x + y

# Asking the user to type the first number
num1 = int(input("Type the first number: "))

# Asking the user to type the second number
num2 = int(input("Type the second number: "))

# Printing the returned value
print(str(num1) + " + " + str(num2) 
      + " = " + str(add_2_numbers(num1, num2)))
