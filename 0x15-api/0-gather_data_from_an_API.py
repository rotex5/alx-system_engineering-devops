#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


def get_details(id):
    """ get task completed"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = id
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "users/{}/todos".format(user_id)).json()

    completed_task = []
    for task in todos:
        if task.get('completed') is True:
            completed_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_task), len(todos)))
    for task in completed_task:
        print("\t {}".format(task))


if __name__ == "__main__":
    get_details(argv[1])
