from datetime import datetime, timedelta

from config import (TASK_1,
                    TASK_2,
                    TASK_3,
                    TASK_4,
                    TASK_5,
                    TASK_6,
                    TASK_7,
                    TASK_8,
                    )

def generate_todo_file(start_date, end_date, tasks, filename):
    # Convert the input dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Define task categories
    everyday_tasks = tasks.get("everyday", [])
    workday_tasks = tasks.get("workday", [])
    special_tasks = tasks.get("special", {})
    
    # Open the file for writing
    with open(filename, 'w') as file:
        # Iterate through each date from start_date to end_date
        current_date = start_date
        while current_date <= end_date:
            # Write the date in YYYY-MM-DD format
            file.write(f"{current_date.strftime('%Y-%m-%d')}:\n")
            
            # Write everyday tasks
            for task in everyday_tasks:
                file.write(f"    ☐ {task}\n")
            
            # Write workday tasks if the current date is a weekday
            if current_date.weekday() < 5:  # Monday is 0, Sunday is 6
                for task in workday_tasks:
                    file.write(f"    ☐ {task}\n")
            
            # Write special tasks for specific days (e.g., Wednesday and Sunday)
            weekday_name = current_date.strftime('%A')
            if weekday_name in special_tasks:
                for task in special_tasks[weekday_name]:
                    file.write(f"    ☐ {task}\n")
            
            file.write("\n")
            # Move to the next day
            current_date += timedelta(days=1)

# Enter date range and tasks
start_date = "2024-07-01"
end_date = "2024-10-01"
tasks = {
    "everyday": [TASK_1, TASK_2, TASK_3, TASK_4, TASK_5, TASK_6],
    "workday": [TASK_7],
    "special": {
        "Wednesday": [TASK_8],
        "Sunday": [TASK_8]
    }
}
filename = "daily_tasks.TODO"

generate_todo_file(start_date, end_date, tasks, filename)
print(f"{filename} has been created successfully!")
