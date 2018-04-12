#Task Manager Program

print('WHAT WOULD YOU LIKE TO DO?')
print("1. Add a task")
print("2. Remove a task")
print("3. Mark task complete")
print("4. List tasks")
answer = input('What would you like to do? Enter 1, 2, 3, or 4:   ')

if answer == '1':
    import addtask


elif answer == '2':
    import deletetask

elif answer == '3':
    print('\nTASK COMPLETE!')
    import menu

else:
    if answer == '4':
        import printlist





