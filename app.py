from expensetracker import ExpenseTracker
from cli_app import CLIApp
import argparse

cli = CLIApp()

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command", help="Commands")

add_parser = subparsers.add_parser("add", help="add a new expense")
add_parser.add_argument("arguments", type=str, help="Contains info about expense")

update_parser = subparsers.add_parser("update", help="update expense")
update_parser.add_argument("arguments", type=str, help="Contains all info to be updated")

delete_parser = subparsers.add_parser("delete", help="delete expense")
delete_parser.add_argument("arguments", type=str, help="Contains id of expense to be deleted")

view_parser = subparsers.add_parser("list", help="view all expenses")

viewSummary_parser = subparsers.add_parser("summary", help="views summary of expenses")

args = parser.parse_args()

if args.command == "add":
    cli.do_add(args.arguments)

if args.command == "update":
    cli.do_update(args.arguments)

if args.command == "delete":
    cli.do_delete(args.arguments)

if args.command == "list":
    cli.do_view(args.arguments)

if args.command == "summary":
    cli.do_viewSummary(args.arguments)


if __name__ == "__main__":
    cli.cmdloop()