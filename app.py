import cmd, os

class ExpenseTracker(cmd.Cmd):
    intro = 'Welcome to the Expense Tracker Shell'
    prompt = 'expense-tracker>> '
    
    

    def __init__(self):
        super().__init__()
        self.expenses = {}
        self.file = 'expense.csv'


    def do_add(self, arg):
        """Add a new expense: add <amount> <description>"""
        print("added")
    
    def do_update(self, arg):
        """
        Update an existing expense: 
        update <id> <new_amount> <new_description>
        """
        print("updated")
    
    def do_delete(self, arg):
        """Delete an expense: delete <id>"""
        print("deleted")
    
    def do_view(self, arg):
        """
        View all expenses: view
        """
        print("view")
    
    def do_viewSummary(self, arg):
        """
        View a summary of all expenses or all expenses for a specific 
        month for a specific month
        """
        print("viewSummary")

    def do_exit(self, arg):
        """Exit the expense tracker shell: exit"""
        print("Exiting...")
        return True
if __name__ == "__main__":
    ExpenseTracker().cmdloop()
        