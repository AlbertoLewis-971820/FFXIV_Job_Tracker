import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Make function to display job details
def display_jobs():
    #Check if there are any jobs in the list in the job_list.json file
    with open('job_list.json', 'r') as file:
        data = json.load(file)
        jobs = data["jobs"]
        if not jobs:
            print("No jobs available.")
            return
        else:
            for i, job in enumerate(jobs, start=1):
                print(f"{i}. Name: {job['name']}, Level: {job['level']}, Role: {job['role']}")
    
    
def add_job(name,level,role):
    name = input("Enter the job name: ")
    level = input("Enter the job level: ")
    role = input("Enter the job role (Tank, Healer, DPS, etc.): ")

    new_job = {
        "name": name,
        "level" : level,
        "role" : role
    }
    #Append the new job to the job_list.json file
    with open('job_list.json', 'r') as file:
        job_data = json.load(file)
        jobs = job_data["jobs"]
        jobs.append(new_job)
    #Write the updated job list back to the job_list.json file
    with open('job_list.json', 'w') as file:
        json.dump(job_data, file, indent=4)

def delete_job(job_name):
    #Delete a job from the job_list.json file
    with open('job_list.json', 'r') as file:
        job_data = json.load(file)
        jobs = job_data["jobs"]
        #Filter out the job to be deleted
        jobs = [job for job in jobs if job["name"] != job_name]
        #Update the job list
        job_data["jobs"] = jobs
    #Write the updated job list back to the job_list.json file    
    with open('job_list.json', 'w') as file:
        json.dump(job_data, file, indent=4)

    print(f"Job '{job_name}' has been deleted.")



running = True
while running:
    print("Welcome to the FFXIV Job Tracker!")

    print("1. View Job Details")
    print("2. Add New Job")
    print("3. Delete Job")
    print("4. Exit")

    choice =input("Please choose a choice from the following options:")

    if choice == "1":
        
        display_jobs()
        input("Press any key to return to the main menu...")
        clear_screen()
    elif choice == "2":
        add_job(name="",level="",role="")
        

    elif choice == "3":
        job_name = input("Enter the name of the job to delete: ")
        delete_job(job_name)

    elif choice == "4": 
        print("Exiting the program. Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")
        clear_screen()
