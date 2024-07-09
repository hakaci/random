from datetime import datetime, timedelta

from config import (TASK_1,
                    TASK_2,
                    TASK_3,
                    TASK_4,
                    TASK_5,
                    TASK_6,
                    TASK_7,
                    TASK_8,
                    DAILY_TODO_PATH
                    )

def generate_todo_file(start_date, end_date, tasks, file_path):
    # Convert input dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Define task categories
    everyday_tasks = tasks.get("everyday", [])
    workday_tasks = tasks.get("workday", [])
    special_tasks = tasks.get("special", {})
    
    # Open file for writing
    with open(file_path, 'w', encoding='utf-8') as file:
        # Iterate through each date from start_date to end_date
        current_date = start_date
        while current_date <= end_date:
            # Write date in YYYY-MM-DD format
            file.write(f"{current_date.strftime('%Y-%m-%d')}:\n")
            
            # Write everyday tasks
            for task in everyday_tasks:
                file.write(f"    ☐ {task}\n")
            
            # Write workday tasks if current date is a weekday
            if current_date.weekday() < 5:  # Monday is 0, Sunday is 6
                for task in workday_tasks:
                    file.write(f"    ☐ {task}\n")
            
            # Write special tasks for specific days (e.g., Wednesday and Sunday)
            weekday_name = current_date.strftime('%A')
            if weekday_name in special_tasks:
                for task in special_tasks[weekday_name]:
                    file.write(f"    ☐ {task}\n")
            
            file.write("\n")
            # Move to next day
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
file_path = DAILY_TODO_PATH

generate_todo_file(start_date, end_date, tasks, file_path)
print(f"{file_path} has been created successfully!")
