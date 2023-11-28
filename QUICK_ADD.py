
#WILL CREATE TWO DIFFERENT TYPES OF ADDS THAT STORE MULTIPLE TYPES OF DATA

import json

while True:
    qa_input = None
    category = None
    amount = None
    current_exp = None
    with open('home_input.txt', 'r') as infile:

        if infile.read().strip() == "QuickAdd":
            qa_input = input("Please enter the expense you would like to add in this format: Category, Amount. ")
            #Allows for input to be iterated through later
            qa_input = qa_input.split(', ')
            category = qa_input[0]
            amount = float(qa_input[1])
    
    new_exp = {category: amount}
    with open('track_expenses.json', 'r') as infile:
            current_exp = infile.read()

    current_exp = json.loads(current_exp)
    if current_exp == {}:
         with open('track_expenses.json', 'w') as outfile:
            json.dump(new_exp, outfile)

    else:
        if category in current_exp:
            current_exp[category] += amount
        else:
            current_exp[category] = amount 

    with open('track_expenses.txt', 'w') as outfile:
        json.dump(current_exp, outfile)

    print("Successfully added")
            
                  
    
              
        

