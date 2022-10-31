
with open("Tasks.py\Task_7\Phone_Book.txt", "r", encoding="utf=8") as file:
    old_file = file.read()
new_file = old_file.replace("-1", " ")

with open("Tasks.py\Task_7\Phone_Book.csv", "w", encoding="utf=8") as file:
    file.write(new_file)
