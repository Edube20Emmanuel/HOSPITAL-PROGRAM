#Certainly! Here's an updated version of the program with error handling added for input validation and exceptions:

#python
def calculate(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x /y

def main():
    for _ in range(5):
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            operator = input("Enter the operator (+, -, *, /): ")

            if operator not in ("+", "-", "*", "/"):
                raise ValueError("Invalid operator!")

            result = calculate(x,y, operator)

            user_answer = float(input("Enter your answer: "))

            if result == user_answer:
                print("Correct!")
            else:
                print("Wrong!")

            print()  # Add a newline for better readability

        except ValueError as e:
            print("Error:", str(e))
            print("Please enter valid numbers and operator.")
            print()
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            print("Please enter a non-zero denominator.")
            print()
        except Exception as e:
            print("An error occurred:", str(e))
            print("Please try again.")
            print()

if __name__ == '__main__':
    main()

