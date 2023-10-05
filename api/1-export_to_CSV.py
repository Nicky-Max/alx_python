import requests
import sys
import csv

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    """ Fetch employee data"""
    employee = requests.get(base_url).json()
    user_id = employee["id"]
    username = employee["username"]

    """ Fetch TODO list for the employee"""
    todos = requests.get(todos_url).json()

    """ Export data in CSV format"""
    csv_file_path = "{}.csv".format(user_id)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for todo in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })

    print(f"Data exported to {csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_data(employee_id)