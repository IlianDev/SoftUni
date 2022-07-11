command = input()

todo_list = [0] * 10
while command != 'End':
    importance, task = command.split("-")
    importance = int(importance) - 1
    todo_list.insert(importance, task)

    command = input()

print([element for element in todo_list if element != 0])
