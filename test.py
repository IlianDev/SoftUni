command = input()

todo_list = [0] * 10
while command != 'End':
    importance, task = command.split("-")
    importance = int(importance) - 1
    todo_list.insert(importance, task)

    command = input()

print(todo_list)
