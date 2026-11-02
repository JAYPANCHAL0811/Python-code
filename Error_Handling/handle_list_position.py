number_list = [15, 28, 42, 57, 73]
try:
    position = int(input("Enter an index from 0 to 4: "))
    print("Value:", number_list[position])
except IndexError:
    print("Index is out of range.")
except ValueError:
    print("Please enter an integer.")
