def print_list():
    """prints an enumerated list of tasks"""
    print('\nHere is your task list:')
    taskfile3 = open('tasks.txt', 'r+')
    for index, line in enumerate(taskfile3, 1):
        print('{:2}.'.format(index), line.rstrip())
    taskfile3.close()
    import menu

print_list()
