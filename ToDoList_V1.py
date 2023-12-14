def put_task():
    print("\t\tType a requirement task: ")
    task = input()
    if len(task) == 0:
        print("You didn't write anything, please write something ")
        put_task()
    else:
        to_do_list.append(task)
        print("Task is added successfully, do you want to add another? : (yes/no)")
        while True:
            task_ask = input()
            if task_ask == "yes":
                put_task()
            if task_ask == "no":
                print("Your current tasks is: ")
                for i in range(len(to_do_list) - 1):
                    print(f"{to_do_list[i]}", end=",")
                print(to_do_list[-1], end="")
                exit()
            else:
                print("Invalid answer, please answer (yes/no)")


print("\n\t\t\tWelcome to ToDo app")
to_do_list = []
if len(to_do_list) == 0:
    print("\t\tYour list is empty, do you want to add the task? : (yes/no)")
else:
    print(f"Your current tasks is {to_do_list}")
while True:
    start = input()
    if start == "yes":
        put_task()
    if start == "no":
        print(f"\t\tYour ToDo list tasks is {to_do_list}")
        print("\n\t\tGoodbye!")
        exit()
    else:
        print("Incorrect value, please type another!")
