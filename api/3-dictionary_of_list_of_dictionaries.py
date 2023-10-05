#!/usr/bin/python
""" import modules"""
""" import requests module"""
import requests
""" import sys"""
import sys
""" import json"""
import json

"""
Get the employee ID from the command line arguments
"""
employee_id = sys.argv[1]
""" 
Define the base URL for the API
"""
base_url = "https://jsonplaceholder.typicode.com/users/"

""" Get the employee details from the API"""
employee = requests.get(base_url + employee_id).json()

""" Get the employee name"""
employee_name = employee["name"]
""" Get the employee TODO list from the API"""
todos = requests.get(base_url + employee_id + "/todos").json()

""" Initialize the total and done tasks counters"""
total_tasks = 0
done_tasks = 0
""" Initialize a list for tasks"""
done_tasks_list = []

"""
 Loop through the todos list and update the counters and tasks list
 """
for todo in todos:
    total_tasks += 1
    if todo["completed"]:
        done_tasks += 1
        done_tasks_list.append({"username": employee_name, "task": todo["title"], "completed": True})
    else:
        done_tasks_list.append({"username": employee_name, "task": todo["title"], "completed": False})

print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))

for title in [task["task"] for task in done_tasks_list if task["completed"]]:
    print("\t " + title)

""" Export data in JSON format"""
output_data = {employee_id: done_tasks_list}
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=2)