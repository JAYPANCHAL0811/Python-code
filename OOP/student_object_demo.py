class Student:
    def display(self):
        print("Name:", self.person_name)
        print("Roll number:", self.roll_number)

student_obj = Student()
student_obj.person_name = "Ananya Sharma"
student_obj.roll_number = 2314
student_obj.display()
