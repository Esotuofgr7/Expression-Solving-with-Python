class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression
        self.result = None

    def evaluate(self):
        try:
            self.result = eval(self.expression)
        except Exception as e:
            self.result = f"Error: {str(e)}"

    def display(self):
        print(f"🔢 Expression: {self.expression}")
        print(f"✅ Result: {self.result}")

# Example usage
if __name__ == "__main__":
    expr_input = input("Enter a mathematical expression (e.g., 2 + 3 * (4 - 1)): ")
    solver = ExpressionSolver(expr_input)
    solver.evaluate()
    solver.display()
