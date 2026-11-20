#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base), params={"userId": user_id}).json()
    done = [t.get("title") for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
