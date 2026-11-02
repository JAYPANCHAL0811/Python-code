class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    def show_name(self):
        print("Name:", self.person_name)

class Student(Person):
    def show_course(self):
        print("Course: BSc IT")

student_obj = Student("Ishaan Mehta")
student_obj.show_name()
student_obj.show_course()
