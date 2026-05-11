
class Student:
    
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
    
    @classmethod
    def from_string(cls,data):
        name,age,location = data.split("|")
        name = name.strip()
        age = age.strip()
        if not age.isdigit():
            raise ValueError("Age must be numeric")
        else:
            age = int(age)
        location = location.strip()
        
        return cls(name,age,location)

s1 = Student.from_string("bhuvi | 23 | Chennai")

print(s1.name)
print(s1.age)
print(s1.location)