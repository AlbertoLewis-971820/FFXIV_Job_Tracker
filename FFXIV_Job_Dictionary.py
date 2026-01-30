jobs = []

#Make function to display job details
def display_jobs():
    if not jobs:
        print("There are no jobs available please add one.")
    else:
        for job in jobs:
            print(f"Job Name: {job['name']}, Level: {job['level']}, Role: {job['role']}")

def add_job(name,level,role):
    name = input("Enter the job name: ")
    level = input("Enter the job level: ")
    role = input("Enter the job role: ")
    new_job = {
        "name": name,
        "level": level,
        "role": role
    }
    jobs.append(new_job)



running = True
while running:
    print("Welcome to the FFXIV Job Dictionary!")

    print("1. View Job Details")
    print("2. Add New Job")
    print("3. Exit")

    choice =input("Please choose a choice from the following options:")

    if choice == "1":
        display_jobs()
    elif choice == "2":
        add_job(name="",level="",role="")

    elif choice == "3": 
        print("Exiting the program. Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")
