class Test:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializing object")

t = Test()
