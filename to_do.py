# making a simple to_do list
todo = "random"

data = list()


def showlist():
    print("Menu:")
    print("1. Add Task:")
    print("2. Task delete:")
    print("3. List of task:")
    print("4. List of completed task:")
    print("5. List of pending task:")
    print("6. Mark as completed task: ")


while todo != '6':
    showlist()
    todo = input("Enter a to_do: ")

    if todo == '1':
        todo = input("Add task: ")
        data.append(todo)
        print("Add task: ", todo)

    elif todo == '2':
        todo = input("which task do you want delete: ")
        if todo in data:
            data.remove(todo)
            print("remove todo: ", todo)
        else:
            print("to_do not present in list")

    elif todo == '3':
        print(" show list of task: ", todo)
        for todo in data:
            print("to_do", todo)
        print("list of task: ", todo)

    elif todo == '4':
        print("list of complete task: ", todo)
        for todo in data:
            print("to_do", todo)

    elif todo == '5':
        todo = input("list of pending task: ")
        if todo not in data:
            print("to_do is pending: ", todo)
        else:
            print("to_do is completed: ")

    elif todo == '6':
        todo = input("keep marked task: ")
        if todo in data:
            print("Marked the task done: ", todo)
        else:
            print("keep marked to done task")













