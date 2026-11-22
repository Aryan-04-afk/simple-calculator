"""Simple command-line calculator."""

WELCOME_MESSAGE = "Hello! Let's do some math."


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operator: {op}")
    return OPERATIONS[op](a, b)


def main():
    print(WELCOME_MESSAGE)
    print("Enter an expression like: 4 + 5   (type 'q' to quit)")
    while True:
        line = input("> ").strip()
        if line.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        parts = line.split()
        if len(parts) != 3:
            print("Please use the format: <number> <operator> <number>")
            continue
        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            print("=", calculate(a, op, b))
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
