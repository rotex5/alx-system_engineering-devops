#!/usr/bin/python3
"""
script that, using this REST API, for all employee IDs,
returns information about his/her TODO list progress and
export to json
"""
import json
import requests


def generate_json(id):
    """ save query to json file"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = id
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "users/{}/todos".format(user_id)).json()

    task_list = []
    sub_task_dict = dict()

    for task in todos:
        sub_task_dict = {"task": "{}".format(
            task.get("title")), "completed": task.get("completed"),
            "username": "{}".format(user.get("username"))}

        task_list.append(sub_task_dict)
    return task_list


def all_details():
    """ get all details """
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    filename = "todo_all_employees.json"
    all_todos = dict()

    for user in users:
        user_id = user.get("id")
        all_todos["{}".format(user_id)] = generate_json(user_id)

    with open(filename, "w") as f:
        json.dump(all_todos, f)


if __name__ == "__main__":
    all_details()
