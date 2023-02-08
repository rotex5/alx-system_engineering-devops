#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export to json
"""
import json
import requests
from sys import argv


def generate_json(id):
    """ save query to json file"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = id
    filename = "{}.json".format(id)
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "users/{}/todos".format(user_id)).json()

    task_list = []
    sub_task_dict = dict()
    main_dict = dict()

    for task in todos:
        sub_task_dict = {"task": "{}".format(
            task.get("title")), "completed": task.get("completed"),
            "username": "{}".format(user.get("username"))}

        task_list.append(sub_task_dict)

    main_dict["{}".format(id)] = task_list

    with open(filename, "w") as f:
        json.dump(main_dict, f)


if __name__ == "__main__":
    generate_json(argv[1])
