t1 = ("Rahul","Kumar","Patel")
t2 = (75,82,90,68,88)

t3 = (t1,t2)

x = input("Enter value: ")

found = False

for i in t3:
    if x in i:
        found = True

if found:
    print("Found")
else:
    print("Not Found")