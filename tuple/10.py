name = "Rahul"
hobbies = ("Reading","Music")
friends = ("Amit","Neha")
degree = "BCA"

t4 = (name,hobbies,friends,degree)

x = input("Enter element: ")

found = False

for i in range(len(t4)):

    if type(t4[i]) == tuple:
        if x in t4[i]:
            print("Found at",i)
            found = True

    else:
        if x == t4[i]:
            print("Found at",i)
            found = True

if found == False:
    print("Not Found")