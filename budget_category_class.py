#Task 1 Define Budget Category Class

'''
In task 1 I defined the BudgetCategory class and initialized it with the self attribute as well as private attributes for category_name and allocated_budget. In task 2 I will define getter and setter methods for them
so they can continue to fucntion properly as private attributes without raising an AttributeError.

Revision: I later had to add attributes for expense total and remaning budget for Task 4 so I initialized those as well with a private attribute of expense total that is keyed to automatically start at - and a remaining budget attribuute that will initialize at the same starting value as the starting budget.
Allocated budget was renamed starting budget
'''
import re

class BudgetCateory:
    
    def __init__(self, category_name, starting_budget):
        self.__category_name = category_name
        self.__starting_budget = starting_budget
        self.__expense_total = 0
        self.__remaining_budget = starting_budget
    
    def get_category_name(self):
        return self.__category_name
    
    def get_starting_budget(self):
        return self.__starting_budget
    
    def get_expense_total(self):
        return self.__expense_total
    
    def get_remaining_budget(self):
        return self.__remaining_budget
    
    def set_category_name(self, new_name):
        if re.match(r"^[A-Za-z_ ]+$", new_name):
            self.__category_name = new_name
        else:
            print("Please ensure new category name is a word coposed of letters, spaces, and underscores.")
        
    def set_starting_budget(self, new_budget):
        if new_budget > 0:
            self.__starting_budget = new_budget
        else:
            print("Budget should be a positive number")
    
    def set_expense_total(self, new_expense_total):
        if self.get_starting_budget() >= new_expense_total > 0:
            self.__expense_total = new_expense_total
        else:
            print("Please ensure total expenses have not gone past starting budget amount and that all inputs are positive and valid.")
    
    def set_remaining_budget(self, new_remaining_budget):
        if self.get_starting_budget() >= new_remaining_budget >= 0:
            self.__remaining_budget = new_remaining_budget
        else:
            print("Please ensure that the remaining budget is is less than or equal to starting budget but not less than zero.")
        
    def add_expense(self, amount):
        if self.get_remaining_budget() >= amount > 0 and (amount + self.get_expense_total()) < self.get_starting_budget():
            self.set_expense_total(self.get_expense_total() + amount)
            self.set_remaining_budget(self.get_remaining_budget() - amount)
            print(f"An expense of {amount} has been categorized as a(n) {self.get_category_name()} expense, leaving the remaining allocated budget at {self.get_remaining_budget()} for that category")
        elif amount > self.get_starting_budget() or amount > self.get_remaining_budget():
            print("This expense is greater than your allocated budget for this category")
        else:
            print("Please ensure a positive input, I have yet to see any expense truly free in this world!")

    def display_category_method(self):
        print(f"Category Name: {self.get_category_name()}\nStarting Budget: {self.get_starting_budget()}\nTotal Expenses for Category: {self.get_expense_total()}\nRemaining Budget for Category: {self.get_remaining_budget()}")

#Task 2 Define Getter and Setters
'''
For Task 2 I defined getters for both private attributes, category_name and allocated_budget by simply returning the self.__category_name or self.__allocated_budget attributes to avoid AttributeErrors.
In defining the setters for these two attributes I used data validation, fist with set_category_name by doing a regex statement where if our new_name is composed of at least 1 or more lower case, uppercase, space character, or underscores it will present a True return to a re.match().
Once this validation is passed we can simply reassign self.__category_name to new_name.
Similarly for set_alloacted_budget if the new_budget is greater than zero it will be counted as a positive number and then can be used to reassign the self.__allocated_budget as new_budget.

Revision: I added getters and setters for expense total and remaining budget ensuring that both stay in between the starting budget and zero when they are set. Allocated budget was renamed starting budget
'''  
#Task 3 Add Expense Method
'''
Our add_expense method works first by ensuring that our new expense is within the remaining budget and a valid input by ensuring it is greater than zero but is less than or equal to the current allocated budget using the self.get_remaiing_budget method. I also added an and statement ensuring the amount when added to total expenses will not exceed the starting budget.
If this returns as true we call the self.set_remaining_budget method with a new budget parameter that is equal to the current get_remaining_budget amount minus the amount we use to call the add_expense method. Before that I also reset total expenses with the self.et_total_expenses method adding on the amount.
After that I use an f-string to print the amount of the expense that is added, what category the expense is being categorized as, and the new remaining budget amount.
I have an elif statement to account for expenses greater than the starting or remainig budget, and then an else statement to catch any negative or zero entries as every expense does cost at least a penny!
'''

#Task 4 display_category_method
'''
For Display category method to work seamlessly I reworked all my earlier code splitting the initial allocated_budget parameter into three separate parameters: a starting_budget, a total_expenses, and a remaining_budget.
Once those were initializd and reworked throughout the code I created an f string that prints the category name, starting budget, total expenses, and remaining budget all on separate lines.
'''