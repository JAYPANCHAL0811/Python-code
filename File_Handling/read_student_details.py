with open("student.txt", "w") as opened_file:
    opened_file.write("Name: Ananya Sharma\nCourse: BSc IT\n")
with open("student.txt", "r") as opened_file:
    print(opened_file.read())
