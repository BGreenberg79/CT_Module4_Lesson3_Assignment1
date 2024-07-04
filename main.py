from budget_category_class import BudgetCateory
import re

budget_list = []

def main_menu():
    while True:
        print("Welcome to our budget management system!")
        main_menu = input("1) Add budget category\n2) Add expense\n3) Display all budget category details\n4) Quit\nEnter Choice: ")
        if main_menu == "1":
            category_name = input("New category name: ")
            starting_budget = int(input("Enter starting budget: "))
            if re.match(r"^[A-Za-z_ ]+$", category_name) and starting_budget > 0:
                new_category = BudgetCateory(category_name, starting_budget)
                budget_list.append(new_category)
                print(f"{new_category.get_category_name()} has been added to the budget list!")
            else:
                print("Please ensure a posiive starting budget and a name using letters, spaces, and underscores were entered for inputs")
        elif main_menu == "2":
            expense_category = input("Enter category of expense: ")
            expense_amount = int(input("Enter amount of expense: "))
            for budget_cat in budget_list:
                if expense_category.lower() == budget_cat.get_category_name().lower() and expense_amount > 0:
                    budget_cat.add_expense(expense_amount)
                else:
                    print("Please ensure category entered has already been added to the list.")
        elif main_menu == "3":
            for category in budget_list:
                category.display_category_method()
                print("\n")
        elif main_menu == "4":
            break
        else:
            print("Please ensure valid input from 1 to 4")
    
main_menu()

'''
In this main.py file I start by importing our BudgetCategory class from budget_category_class.py and I also import the regex re module so I can use re.match in validating the input of our category name.
I initialize an empty budget_list that will house our different categories once we add them as class objects. In the main_menu I create an input that allows users to hoose one of four options. First they can add 
a new category where they will be prompted for a new category name and starting budget. These two inputs are validated to match a regular expression of spaces, underscores, and letters for category and an integer over zero for starting budget.
If they are not an error message is printed but if they are we create a new_category variable that houses a BudgetCategory class object holding our name and starting budget as attributes. This object is then appended to our list.
If the user selects option 2, to enter an expense, they are prompted for inputs of category of expese and the amount of expense. I then loop thorugh every object in our list and if the lower case of our user input matches the lower case of any get_category_name method from our object list,
as well as the amount input being over zero, we will then run the add_expense method on that object from the list with the attribute of our expense_amount integer input. Otherwise I ask the suer to ensure they have already added this category.
If the user enters 3, to display each category in our budget, I run a simple for loop for every category in our budget list where the display category method is used on each object and an empty \n line break is printed between entries to make it user fiendly.
Lastly 4 breaks our while loop and any other input asks for a valid input numbered 1 to 4.  
'''