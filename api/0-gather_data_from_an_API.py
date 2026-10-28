#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    done = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
