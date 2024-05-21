#!/usr/bin/python3
"""
export all employees todos data in the JSON format.
"""

import json
import requests

if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users/"
    response_users = requests.get(url_users)
    users = response_users.json()

    dictionary = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url_todos = (
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/')
        response_todos = requests.get(url_todos)
        tasks = response_todos.json()

        dictionary[user_id] = []

        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
