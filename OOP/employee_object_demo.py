class Employee:
    def __init__(self, person_name, monthly_salary):
        self.person_name = person_name
        self.monthly_salary = monthly_salary

    def display(self):
        print("Name:", self.person_name)
        print("Salary:", self.monthly_salary)

staff_one = Employee("Rajesh Kumar", 45000)
staff_two = Employee("Sneha Joshi", 52000)
staff_one.display()
staff_two.display()
