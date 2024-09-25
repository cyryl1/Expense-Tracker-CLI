import json
import datetime
import pandas as pd

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
    
    def list(self):
        """
        View all expenses: view
        """
        
        with open(self.file, 'r') as f:
            data = json.load(f)

            if data:
                # headers = ["ID", "Description", "Amount", "Date", "Update Date"]
                # table = tabulate.tabulate(data, headers, tablefmt="plain")
                # print(table)
                pd.set_option('display.max_colwidth', 100)
                pd.set_option('display.width', 1000)

                df = pd.json_normalize(data)
                print(df.to_string(index=False))
            else:
                print("No expenses found")
    
    def viewSummary(self, arg):
        """
        View a summary of all expenses or all expenses for a specific 
        month for a specific month
        """
        with open(self.file, 'r') as f:
            data = json.load(f)
        if arg is None:
                total_amount = sum(float(expense["Amount"].replace("$", "")) for expense in data)
                print(f"Total expenses: ${total_amount}")
        elif arg:
            try:
                month = int(arg)
                current_year = datetime.datetime.now().year
                filtered_data = [
                    expense for expense in data
                    if datetime.datetime.strptime(expense["Date"], "%Y-%m-%d").month == month and
                    datetime.datetime.strptime(expense["Date"], "%Y-%m-%d").year == current_year
                ]
                total_amount = sum(float(expense["Amount"].replace("$", "")) for expense in filtered_data)
                print(f"Total expense for month {month}: ${total_amount:.2f}")
            except ValueError:
                print("Invalid date format. Please use --month <months-number>")
            
        