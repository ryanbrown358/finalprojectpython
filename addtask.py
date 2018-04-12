def add_task():
    """This function adds an input task to the TaskList.txt file"""

    yourTask = []
    line = input("Add your task: ")
    yourTask.append(line)
    taskfile = open('tasks.txt', 'a')
    for line in yourTask:
        taskfile.write("%s\n" % line)
    taskfile.close()

    import menu


add_task()
