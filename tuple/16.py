st = ("Pen","Marker","Pencil","Eraser","Scale")

for word in st:

    rev = ""

    for ch in word:
        rev = ch + rev

    print(rev)