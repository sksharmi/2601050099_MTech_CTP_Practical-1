from dataclasses import dataclass

# Using dataclass
@dataclass
class Employee:
    name: str
    age: int
    salary: float

# Traditional class
class Employee2:
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

e1 = Employee("Ravi", 25, 30000.0)
e2 = Employee2("Ravi", 25, 30000.0)

print(e1)
print(e2.name, e2.age, e2.salary)