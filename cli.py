import json
tasks = {}

# reload tasks
def reload_tasks():
    global tasks
    try:
        with open ("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
            print()
            print("No data added yet.")

 # update tasks
def up_tasks():
    with open("tasks.json", "w") as wf:
        json.dump(tasks, wf)
        

# 1 add function
def add_task(id):
    while True:
        title = input("Title: ").title().strip()     # title
        
        while True:
            priority = input("Priority(low, medium, high): ").lower().strip()      # priority
            if priority not in ("low", "medium", "high"):
                print()
                print("Wrong priority. Try again?")
                continue
            break     #  priority break
            
        while True:
            status = input("Status (pending/ completed): ").strip().lower()
            if status not in ("pending", "completed"):
                print()
                print("Wrong status. Try again?")
                continue
            break
            
        tasks[int(id)] = { "title": title,
            "priority": priority,
            "status": status}
        up_tasks() # call update_tasks
           
        break # main break
                
                
# 2 view tasks
def  view_tasks():
    if tasks:
        for index, value in enumerate(tasks, 1):
            print(f"{index}. Id:{value}, title: {tasks[value]['title']}, priority: {tasks[value]['priority']}, status: {tasks[value]['status']}")
    else:
        print("No tasks added yet.")
                    
                           
# 3 update task       
def update_task():
    if tasks:
        check = 0
        print("Available Tasks:") # check available task
        view_tasks() #call view task for view tasks
        print()
        while True:
            select_id = input("Select an id number: ")
            if check == 4:
                print()
                print("Too many wrong attempts. Try again in few minutes?")
                break
            if select_id in tasks:
                print()
                print("Your request successfully match. You can now update following information")
                print()
                add_task(select_id)
                up_tasks()
                
                    
            else:
                print()
                print(f"Id: ({select_id}) didn't found.")
                check += 1
                continue  
            break
    else:
        print()      
        print("No data found.") 
    
                 
               
# delete tasks
def delete_tasks():
    print("Available Tasks: ")
    view_tasks()
    main_wrong = 0
    wrong_title = 0
    while True:
        if tasks:
            print()
            select_id = input("Id number: ")
            if main_wrong == 4:
                print()
                print(f"You have tried ({main_wrong}) wrong attempts so we block you due to security concern. Try again in few minutes.")
                break
            if select_id in tasks:
                print()
                while True:
                    select_title = input("Title: ").title().strip()
                    if wrong_title == 4:
                        print()
                        print(f"You have tried ({wrong_title}). Try again in few minutes.")
                        break
                    if select_title == tasks[select_id]["title"]:
                        print()
                        del tasks[select_id]
                        up_tasks()
                        print(f"Successfully deleted id: {select_id} title: {select_title}.")
                        break
                    elif select_title == "":
                        print()
                        print("Oops you enter an space. Try again?")
                        wrong_title += 1
                        continue
                    else:
                        print()
                        print(f"{select_title} didn't matched.")
                        wrong_title += 1
                        continue
                
            else:
                print()
                print(f"Selected id number({select_id}) didn't found.")
                main_wrong += 1
                continue
            break
        else:
            print("Please added it first.")   
            break                                                 
   
                
        

reload_tasks()
while True:
    print() # Our options and services
    print("1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    print()
    try: # input from user with validation.
        user_choice = int(input("Select an option (1-5): "))
    except ValueError:
        print()
        print(" Select an option from 1 upto 5.")
    
    # add condition
    if user_choice == 1:
        id = max((int(k) for k in tasks.keys()), default=0) + 1
        
        print("ID:",id)  
        add_task(id)    #call add_function
    elif user_choice == 2:
        view_tasks()    # call view_tasks
    elif user_choice == 3:
        update_task()    # call update_task
    elif user_choice == 4:
        delete_tasks()  # call delete_task    
    elif user_choice == 5:
        print()
        print("Successfully exit. Thanks for using our service.")
        up_tasks()
        break
    else:
        print()
        print(" Select an option from 1 upto 5.")
        continue
    
