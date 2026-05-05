# class variable vs instance variable

class Company:
    
    company_name = "ABC Corp"
    
    def __init__(self,name):
        self.employee_name = name


c1 = Company("John")
c2 = Company("Doe")

c1.company_name = "Corp"

print(c1.company_name)
print(c2.company_name)