def put_task():
    print("\t\tType a requirement task: ")
    task = input()
    print("\t\tPrint the position of task: ")
    position = int(input())
    if len(task) == 0:
        print("You didn't write anything, please write something ")
        put_task()
    else:
        to_do_list[position] = task
        print("Task is added successfully, do you want to add another? : (yes/no)")
        while True:
            task_ask = input()
            if task_ask == "yes":
                put_task()
            if task_ask == "no":
                print(f"Your current tasks is: {to_do_list} ")
                quiz()
                exit()
            else:
                print("Invalid answer, please answer (yes/no)")


def quiz():
    print("\t\tDo you wanna remove any tasks?: (yes/no) ")
    while True:
        quiz_answer = input()
        if quiz_answer == "yes":
            del_task()
        if quiz_answer == "no":
            print("ok, as you wish")
            print("Bye!")
            return
        else:
            print("Invalid answer, please type (yes/no)")


def del_task():
    if len(to_do_list) == 0:
        print("Your list is already empty, do you want to add any task?")
        while True:
            zero_len_ask = input("(yes/no):")
            if zero_len_ask == "yes":
                put_task()
            if zero_len_ask == "no":
                print("Your ToDoList is empty, good job :)")
                exit()
            else:
                print("Invalid option, please type (yes/no)")
    print(f"\t\t{to_do_list}")
    while True:
        print("\t\tChoose the position to remove")
        del_ask = int(input())
        if del_ask in to_do_list.keys():
            to_do_list.__delitem__(del_ask)
            print("\t\tDo you want to delete another task?: (yes/no)")
            while True:
                repeat_del = input()
                if repeat_del == "yes":
                    del_task()
                if repeat_del == "no":
                    print(f"Your updated list is: {to_do_list}")
                    print("Goodbye!")
                    exit()
                else:
                    print("Invalid option, please type (yes/no)")
        else:
            print("\t\tInvalid key, please type a correct key!")


print("\n\t\t\tWelcome to ToDo app")
to_do_list = {}
if len(to_do_list) == 0:
    print("\t\tYour list is empty, do you want to add the task? : (yes/no)")
else:
    print(f"\t\tYour current tasks is {to_do_list}")
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
