from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date  # Format: YYYY-MM-DD
        self.amount = float(amount)
        self.category = category
        self.description = description

    def to_dict(self):
        """Convert object to dictionary for JSON saving."""
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense_obj):
        self.expenses.append(expense_obj)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            return self.expenses.pop(index)
        return None

    def get_total_by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category.lower() == category.lower())

    def get_all_expenses(self):
        return self.expenses
    
    def __init__(self):
        self.expenses = []
        self.budgets = {}  # Format: {"Category": limit_amount}

    def set_budget(self, category, limit):
        self.budgets[category.title()] = float(limit)

    def get_budget_status(self, category):
        """Returns (spent, limit, is_over) for a category."""
        spent = sum(e.amount for e in self.expenses if e.category.title() == category.title())
        limit = self.budgets.get(category.title(), 0)
        is_over = spent > limit if limit > 0 else False
        return spent, limit, is_over