#!/usr/bin/python3
"""
export employee data in the json format to json file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/"

    response = requests.get(url)
    username = response.json().get("username")
    user_id = sys.argv[1]

    response = requests.get(url + "todos")
    employee_todos = response.json()

    dic = {user_id: []}
    for task in employee_todos:
        dic[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open(f'{user_id}.json', 'w') as file:
        json.dump(dic, file)
