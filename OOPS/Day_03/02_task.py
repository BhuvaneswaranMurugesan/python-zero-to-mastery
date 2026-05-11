class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls,data):
        name,age = data.split("-")
        return cls(name,int(age))

s1 = Student.from_string("bhuvi-23")
print(s1.name)
print(s1.age)
