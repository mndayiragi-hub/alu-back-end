#!/usr/bin/python3
"""Exports an employee's TODO list to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [user_id, user["username"], t["completed"], t["title"]])
