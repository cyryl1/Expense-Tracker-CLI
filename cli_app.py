import cmd
from expensetracker import ExpenseTracker
import shlex

expense = ExpenseTracker()

class CLIApp(cmd.Cmd):
    intro = "Welcome to expense tracker app"
    prompt = "expense-tracker>> "

    def __init__(self):
        super().__init__()

    def do_add(self, args):
        """Add a new expense: add <amount> <description>"""
        args = shlex.split(args)
        if '--description' in args:
            description_index = args.index("--description") + 1
            description = args[description_index]

        if '--amount' in args:
            amount_index = args.index("--amount") + 1
            amount = float(args[amount_index])
            try:
                if amount > 0:
                    expense.add(description, amount)
                else:
                    print("Amount cannot be negative")
            except ValueError:
                print("Amount cannot be negative")

    def do_update(self, args):
        """
        Update an existing expense: 
        update <id> <new_amount> <new_description>
        """
        args = shlex.split(args)
        if "--id" in args:
            id_index = args.index("--id") + 1
            id = int(args[id_index])
        else:
            print("Id must be present")

        description = None
        amount = None
            

        if "--description" in args:
            description_index = args.index("--description") + 1
            description = args[description_index]
        elif "--amount" in args:
            amount_index = args.index("--amount") + 1
            amount = args[amount_index]
        elif "--description" in args and "--amount" in args:
            description_index = args.index("--description") + 1
            description = args[description_index]

            amount_index = args.index("--amount") + 1
            amount = args[amount_index]
        else:
            print("A description or an amount must be present or both")

        expense.update(id, description, amount)
        
        
    
    def do_delete(self, args):
        """Delete an expense: delete <id>"""
        args = shlex.split(args)

        if "--id" in args:
            id_index = args.index("--id") + 1
            id = int(args[id_index])
        else:
            id = None
        
        expense.delete(id)
    
    def do_list(self, args):
        """
        View all expenses: view
        """
        if args:
            print("No argument needed use View instead")
        else:
            expense.list()
    
    def do_summary(self, args):
        """
        View a summary of all expenses or all expenses for a specific 
        month for a specific month
        """
        args = shlex.split(args)
        if '--month' in args:
            month_index = args.index("--month") + 1
            month = args[month_index]
            expense.viewSummary(month)
        else:
            expense.viewSummary(None)
    def do_exit(self, args):
        """Exit the expense tracker shell: exit"""
        print("Exiting...")
        return True