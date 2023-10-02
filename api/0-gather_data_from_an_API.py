#!/usr/bin/python
"""
import requests and sys
"""

import requests
import sys
"""
define a function 
"""

def get_employee_data(employee_id):
     """
     Fetch employee details
     """
     employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
     employee_response = requests.get(employee_url)
     employee_data = employee_response.json()

    # Fetch employee TODO list
     todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
     todos_response = requests.get(todos_url)
     todos_data = todos_response.json()

     return employee_data, todos_data
"""
define a function
"""
def display_todo_progress(employee_data, todos_data):
    employee_name = employee_data['name']
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    
    for task in done_tasks:
        print("\t{}".format(task['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    
    try:
        employee_data, todos_data = get_employee_data(employee_id)
        display_todo_progress(employee_data, todos_data)
    except requests.exceptions.RequestException as e:
        print("Error: {}".fomart(e))