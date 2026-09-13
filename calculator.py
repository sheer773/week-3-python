class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero not allowed!"
        except Exception as e:
            return f"Error: {e}"

calc = Calculator()
try:
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    print("Add:", calc.add(x,y))
    print("Div:", calc.div(x,y))
except ValueError:
    print("Please enter only numbers!")