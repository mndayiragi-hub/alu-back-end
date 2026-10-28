#!/usr/bin/python3
"""Exports all employees' TODO lists to a single JSON file."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    data = {}
    for user in users:
        data[str(user["id"])] = [
            {"username": user["username"],
             "task": t["title"],
             "completed": t["completed"]}
            for t in todos if t["userId"] == user["id"]
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
