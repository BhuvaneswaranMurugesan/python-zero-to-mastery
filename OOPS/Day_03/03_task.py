class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b!=0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

print(Calculator.add(2, 3))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(4, 5))