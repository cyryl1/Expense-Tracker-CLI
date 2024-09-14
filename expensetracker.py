import json
import datetime

class ExpenseTracker:
    
    

    def __init__(self):
        self.expenses = {}
        self.file = 'expense.json'


    def add(self, description, amount):
        """Add a new expense: add <amount> <description>"""
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        if data:
            next_id = data[-1]['Id'] + 1
        else:
            next_id = 1

        self.expenses['Id'] = next_id
        self.expenses['Description'] = description
        self.expenses['Amount'] = f"${float(amount)}"
        self.expenses['Date'] = datetime.datetime.now().strftime("%Y-%m-%d")
        self.expenses['UpdateDate'] = self.expenses['Date']

        data.append(self.expenses)
        
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"Expense added successfully, ID: {self.expenses["Id"]}")
        
    
    def update(self, id, description=None, amount=None):
        """
        Update an existing expense: 
        update <id> <new_amount> <new_description>
        """
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)

            for expense in data:
                if expense["Id"] == id:
                    if description and amount:
                        expense["Description"] = description
                        expense["Amount"] = f"${float(amount)}"
                    elif description:
                        expense["Description"] = description
                    elif amount:
                        expense["Amount"] = f"${float(amount)}"
                    else:
                        print("Please provide a description or an amount")
                    expense["UpdateDate"] = datetime.datetime.now().strftime("%Y-%m-%d")

                    break

                    

            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Updated Task with ID {id}")
        except IndexError:
            print("Please provide an ID and a new description or amount")
        except ValueError:
            print("ID must be a number")
        except ValueError:
            print("Amount must cannot be negative")
        except FileNotFoundError:
            print("File not found")

        
    
    def delete(self, id):
        """Delete an expense: delete <id>"""
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)

            for expense in data:
                if expense["Id"] == id:
                    data.remove(expense)
                    break
                else:
                    data = []

            with open(self.file, "w") as f:
                json.dump(data, f, indent=4)
        except ValueError:
            print("ID must be a number")
    
    def view(self, arg):
        """
        View all expenses: view
        """
        print("view")
    
    def viewSummary(self, arg):
        """
        View a summary of all expenses or all expenses for a specific 
        month for a specific month
        """
        print("viewSummary")

        