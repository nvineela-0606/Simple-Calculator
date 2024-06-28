def calculate(num1, num2, operator):
  """
  Performs basic arithmetic operations based on the operator.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the operation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Error: Invalid operator"

while True:
  # Get user input
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operator (+, -, *, /): ")

  # Perform calculation
  result = calculate(num1, num2, operator)

  # Print the result
  print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to continue
  user_choice = input("Do you want to continue? (y/n): ")
  if user_choice.lower() != "y":
    break

print("Thank you for using the calculator!")
