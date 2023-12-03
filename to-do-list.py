tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added successfully.')

def view_tasks():
    if not tasks:
        print('No tasks available.')
    else:
        print('Your tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f'Task "{completed_task}" marked as completed.')
    else:
        print('Invalid task index.')

while True:
    print('\nTodo List Menu:')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Complete Task')
    print('4. Exit')

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        task = input('Enter the task: ')
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input('Enter the index of the task to complete: '))
        complete_task(task_index)
    elif choice == '4':
        print('Exiting the Todo List program. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 4.')
