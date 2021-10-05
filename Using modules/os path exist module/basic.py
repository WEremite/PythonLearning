import os

if os.path.exists("files/vegetables.txt"):
    with open("files/vegetables.txt") as file:
        print(file.read())
else:
    print("File does not exist")
