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
# 1 add function
def add_task(tasks_id):
    wrong_title = 0
    wrong_priority = 0
    wrong_status = 0
    while True:
        if wrong_title == 5:
            print()
            print(f"Too many wrong attempts({wrong_title}).Try again in few minutes.")
            return False

        title = input("Title: ").title().strip()     # title

        if title == "":
            print("Space wasn't allowed try again.?")
            wrong_title += 1
            continue
        
        while True:
            if wrong_priority == 5:
                print()
                print(f"Too many wrong attempts({wrong_priority}).Try again in few minutes.")
                return False
            print()
            priority = input("Priority(low, medium, high): ").lower().strip()      # priority
            
            if priority == "":
                print()
                print("No space allowed. Try again.?")
                wrong_priority += 1
                continue
            if priority not in ("low", "medium", "high"):
                print()
                print("Wrong priority. Try again?")
                wrong_priority += 1
                continue       
            
            while True:
                if wrong_status == 5:
                    print()
                    print(f"You have tried ({wrong_status}) wrong attempts. Try again in few minutes later.")
                    return False
                print()
                status = input("Status (pending/ completed): ").strip().lower()    # status
                
                if status == "":
                    print()
                    print("No space allowed. Try again.?")
                    wrong_status += 1
                    continue
                if status not in ("pending", "completed"):
                    print()
                    print("Wrong status. Try again?")
                    wrong_status += 1
                    continue
                break   # status break
            break   # priority break   
        break  # title break
    tasks[str(tasks_id)] = { "title": title,
            "priority": priority,
            "status": status}
    print()
    print(f"Title: {title}, Priority: {priority} and Status: {status}, added successfully.")
    up_tasks() # call update_tasks
    return True
           
        

    
                
                
# 2 view tasks
def  view_tasks():
    if tasks:
        print("Available Tasks:")
        for index, k in enumerate(tasks, 1):
            print(f"{index}. Id:{k}, title: {tasks[k].get('title', 'Something went wrong.')}, priority: {tasks[k].get('priority', 'Something went wrong.')}, status: {tasks[k].get('status', 'Something went wrong.')}")
    else:
        print("No tasks added yet.")
                    
                           
# 3 update task       
def update_task():
    view_tasks() #call view task for view tasks
    print()
    check = 0
    while True:
        if check == 5:
            print()
            print("Too many wrong attempts. Try again in few minutes later?")
            return False
        select_id = input("Select an id number: ")
        
        if select_id == "":
            print()
            print("No space allowed in id number.")
            check += 1
            continue     
        if select_id in tasks:
            print()
            print("Your request successfully match. Now you can update following information")
            print()
            result = add_task(select_id)
            return result
            
        else:
            print()      
            print(f"Id number: {select_id} didn't matched.")
            check += 1
            continue
            
        
    
                 
               
# delete tasks
def delete_tasks():
    view_tasks()
    if tasks:
        wrong_id = 0
        wrong_title = 0
        while True:
            print()
            if wrong_id == 5:
                print()
                print(f"You have tried ({wrong_id}) wrong attempts. Try again in few minutes later.")
                return False
            select_id = input("Id number: ")

            if select_id == "":
                print()
                print("No space allowed in id number.")
                wrong_id += 1
                continue
            
            if select_id in tasks:
                print()
                while True:
                    if wrong_title == 5:
                        print()
                        print(f"You have tried ({wrong_title}). Try again in few minutes.")
                        return False
                    select_title = input("Title: ").title().strip()
                    
                    if select_title == "":
                        print()
                        print("Oops you enter an space. Try again?")
                        wrong_title += 1
                        continue
                    elif select_title == tasks[select_id]["title"]:
                        print()
                        del tasks[select_id]
                        up_tasks()
                        print(f"Id: {select_id} Successfully deleted with title, priority and status.")
                        return True
                    
                    else:
                        print()
                        print(f"Title: {select_title} didn't matched.")
                        wrong_title += 1
                        continue
                
            else:
                print()
                print(f"Id: {select_id} didn't matched.")
                wrong_id += 1
                continue
          
          
            break
        
   
                
        
main_wrong = 0
reload_tasks()
while True:
    print() # Our options and services
    print("1. Add task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    print()
    if main_wrong == 5:
        print()
        print(f"Too many wrong attempts({main_wrong}). Try again in few minutes later.")
        break # main break
        
    try: # input from user with validation.
        user_choice = int(input("Select an option (1-5): "))
    except ValueError:
        print()
        print("Select an option from 1 upto 5.")
        main_wrong += 1   
        continue     
        
    
    if user_choice == 1:   # add condition
        if tasks:
            tasks_id = max(int(k) for k in tasks.keys()) + 1
        else:
            tasks_id = 1       
        print("ID:",tasks_id)  
        add_task(tasks_id)    #call add_function
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
        main_wrong += 1
        continue
    
