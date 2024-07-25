first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter the operator (+,-,/,*): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number/second_number
    else:
        result = "Error! Division by Zero"
else:
    result = "Invalid Operation"

print(f"The result of the operation is: {result}")
