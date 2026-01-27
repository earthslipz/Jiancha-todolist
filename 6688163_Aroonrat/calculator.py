"""
Simple calculator module with basic arithmetic operations.
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_velocity(distance: float, time: float) -> float:
    """Calculate velocity given distance and time. Velocity = distance / time."""
    if time == 0:
        raise ValueError("Time cannot be zero")
    return distance / time


def main():
    """Interactive calculator interface."""
    print("Simple Calculator")
    print("-" * 40)
    
    while True:
        try:
            print("\nOperations: +, -, *, /")
            print("Type 'quit' to exit")
            
            operation = input("Enter operation (+, -, *, /): ").strip()
            
            if operation.lower() == 'quit':
                print("Goodbye!")
                break
            
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please use +, -, *, or /")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
