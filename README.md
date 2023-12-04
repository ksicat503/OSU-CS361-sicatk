# OSU-CS361-sicatk
## QUICK_ADD.PY
File allows to add expenses by reading home_input.txt and adding it to track_expenses.json.

##How to Request Data
To request data, you must write to home_input.txt. You must write to the file in this format:

Category, Amount, Month, Day

- Category is the category/type for the expense
- Amount is how much the cost is
- Month is an optional input. It is either the month in number or written form (12 or December)
- Day is an optional input. It is a number for the day of the month.
- If there is not month in the input, there cannot be a day

QUICK_ADD is always reading home_input.txt and sending the data is tracj_expenses.json and stops until new text is in home_input.txt. To
then recieve data, you must read track_expenses.json and then get the data you want. This is an example of how data is stored in 
track_expenses.json.
```
{
  "May": [
    {
      "Category": "GROCERIES",
      "Amount": "56.73",
      "Day": "7"
    },
    {
      "Category": "FOOD",
      "Amount": "32.89",
      "Day": "9"
    },
    {
      "Category": "RENT",
      "Amount": "1250.0",
      "Day": "None"
    },
    {
      "Category": "GROCERIES",
      "Amount": "2.33",
      "Day": "22"
    }
  ],
  "April": [
    {
      "Category": "TRAVEL",
      "Amount": "175.0",
      "Day": "19"
    }
  ],
  "None": [
    {
      "Category": "FOOD",
      "Amount": "25.0",
      "Day": "None"
    }
  ]
}
```
- Expenses are stored in the same month
- Expenses without a month are stored in their own category, "None", which can be changed later

Here is an example of code that can get data from the month of May. This example adds up the GROCERIES expenses in the month
then prints it
```
import json

with open('track_expenses.json', 'r') as infile:
    expense_data = json.load(infile)

groceries_expenses_total = 0
if "May" in expense_data:
    
    #Iterate through expenses in the month of May
    for expense in expense_data["May"]:
        if expense["Category"] == "GROCERIES":
            groceries_expenses_total += float(expense["Amount"])

print(groceries_expenses_total)
```

![Alt text](https://github.com/ksicat503/OSU-CS361-sicatk/blob/main/readme%20uml.jpeg)
