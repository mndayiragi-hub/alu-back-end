#!/usr/bin/python3
"""Exports an employee's TODO list to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    data = {user_id: [
        {"task": t["title"],
         "completed": t["completed"],
         "username": user["username"]}
        for t in todos
    ]}

    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)
