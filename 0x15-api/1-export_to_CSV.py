#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
and script to export data in the CSV format
"""
import requests
from sys import argv


def generate_csv(id):
    """ export user data to csv"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = id
    filename = "{}.csv".format(id)
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "users/{}/todos".format(user_id)).json()

    with open(filename, "a") as f:
        for task in todos:
            f.write('"{}","{}","{}","{}" \n'.format(
                user_id, user.get('username'),
                task.get('completed'), task.get('title')))


if __name__ == "__main__":
    generate_csv(argv[1])
