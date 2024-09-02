class Employee:
    salary = 34000
    increment = 0.20  # Increment as a float

    @property
    def Salary_After_increment(self):
        return self.salary * (1 + self.increment)

e = Employee()
print(f"Original Salary: {e.salary}")
print(f"Increment: {e.increment * 100}%")
print(f"Salary after increment: {e.Salary_After_increment}")
