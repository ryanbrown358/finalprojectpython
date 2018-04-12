def del_task():
    """This function shows a list and lets user delete a task from the list"""
    import printlist

    deltask = input('What task would you like to delete?').strip()

    with open('tasks.txt', 'r+') as file:
        tasks = file.readline()
        file.seek(0)
        for line in tasks:
            if line is deltask:
                file.write('Deleted')
        file.truncate()

    with open('tasks.txt') as file:
        print(file.read())


del_task()


# range(len(tasks)
