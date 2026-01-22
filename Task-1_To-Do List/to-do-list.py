print("\nReady to plan your day, shravani..?")
def main():
    tasks = []

    while True:
        print("\nLet's organize your task for the dayy...!")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            num_of_tasks = int(input("How may task you want to add for today: "))
            
            for i in range(num_of_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as completed!")
                print("Great job shravani!, One task completed ")

                pending = sum(1 for task in tasks if not task["done"])
                print(f"\n{pending} task(s) are still pending..,Keep going, shravani")

            else:
                print("Invalid task number.")


        elif choice == '4':
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_index]["task"] = new_task
                print("Task updated successfully")
            else:
                print("Invalid task number.")


        elif choice == '5':
            print("You did great today..! Stay consistent, shravani")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
