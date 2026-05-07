
# Instead
"""
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
"""

class Employee:
    
    company_name = "ABC Corp"
    
    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name = new_name

e1 = Employee()
e2 = Employee()

e1.change_company_name("Corp")

print(e1.company_name)
print(e2.company_name)