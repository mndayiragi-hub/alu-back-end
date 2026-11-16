#!/usr/bin/python3
"""
A Python script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import sys
import urllib.request
import json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        
        # Base URL for JSONPlaceholder API
        base_url = "https://jsonplaceholder.typicode.com"
        
        # Fetch user details
        user_url = f"{base_url}/users/{employee_id}"
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())
            employee_name = user_data.get("name")
            
        # Fetch user todos
        todos_url = f"{base_url}/todos?userId={employee_id}"
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())
            
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(completed_tasks)
        
        # Display output in the exact requested format
        print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_tasks}):"
        )
        
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
