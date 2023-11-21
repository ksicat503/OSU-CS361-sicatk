import json

with open('track_expenses.json', 'r') as infile:
    expenses = infile.read()

contents = json.loads(expenses)

print(contents)