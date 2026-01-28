jobs = []
running = True
while running:
    print("Welcome to the FFXIV Job Dictionary!")

    print("1. View Job Details")
    print("2. Add New Job")
    print("3. Exit")

    choice =input("Please choose a choice from the following options:")

    if choice == "1":
        if not jobs:
            print("No jobs available. Please add a new job first.")
        else:
            for job in jobs:
                print(f"Job Name: {job['name']}, Level: {job['level']}, Role: {job['role']}")
        if jobs == {}:
            print("No job details available. Please add a new job first.")
    elif choice == "2":
        name = input("Enter Job Name: ")
        try:
            level = int(input("Enter Job Level: "))
            if level < 1 or level > 100:
                print("Level must be between 1 and 100.")
                continue
        except ValueError:
            print("Invalid level. Please enter a number.")
            continue
        role = input("Enter Job Role: ")
        new_job = {
            "name": name,
            "level": level,
            "role": role
        }
        jobs.append(new_job)
        print("New job added successfully!")
    elif choice == "3": 
        print("Exiting the program. Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")
