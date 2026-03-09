from datetime import datetime
class Reporter:
    @staticmethod
    def generate_budget_report(manager):
        if not manager.budgets:
            print("[!] No budgets set yet. Go to 'Settings' to set limits.")
            return

        print("\n" + "="*60)
        print(f"{'Category':<15} | {'Spent':>10} / {'Limit':<10} | Status")
        print("-" * 60)

        for cat, limit in manager.budgets.items():
            spent, _, is_over = manager.get_budget_status(cat)
            
            # Create a progress bar: [#####-----]
            percent = (spent / limit) * 100 if limit > 0 else 0
            bar_length = 10
            filled = int((percent / 100) * bar_length) if percent <= 100 else bar_length
            bar = "[" + "#" * filled + "-" * (bar_length - filled) + "]"
            
            status = "!! OVER !!" if is_over else "OK"
            print(f"{cat:<15} | ${spent:>9.2f} / ${limit:<9.2f} | {bar} {status}")
        print("="*60)

    @staticmethod
    def generate_monthly_trend(expenses):
        if not expenses:
            print("[!] No data available for trend analysis.")
            return

        # 1. Group by Year-Month
        trends = {}
        for e in expenses:
            # Convert string date to a 'Year-Month' key
            month_key = datetime.strptime(e.date, "%Y-%m-%d").strftime("%Y-%m")
            trends[month_key] = trends.get(month_key, 0) + e.amount

        # 2. Sort months chronologically
        sorted_months = sorted(trends.keys())

        print("\n--- MONTHLY SPENDING TREND ---")
        print(f"{'Month':<15} | {'Amount':>10} | Change")
        print("-" * 45)

        previous_amt = None
        for month in sorted_months:
            current_amt = trends[month]
            
            # 3. Calculate Percentage Change
            if previous_amt is None:
                change_str = "---"
            else:
                change = ((current_amt - previous_amt) / previous_amt) * 100
                symbol = "↑" if change > 0 else "↓"
                change_str = f"{symbol} {abs(change):.1f}%"

            print(f"{month:<15} | ${current_amt:>9.2f} | {change_str}")
            previous_amt = current_amt

    @staticmethod
    def generate_category_summary(expenses):
        """Generates a percentage-based breakdown of spending by category."""
        if not expenses:
            print("\n[!] No expenses found to summarize.")
            return

        # 1. Aggregate totals by category
        category_totals = {}
        for e in expenses:
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount
        
        total_spent = sum(category_totals.values())

        print("\n" + "="*50)
        print(f"{'Category':<20} | {'Amount':>10} | {'Percentage'}")
        print("-" * 50)

        # 2. Display with simple text-bar visualization
        for category, amount in category_totals.items():
            percentage = (amount / total_spent) * 100
            # Visual Bar (1 '#' for every 5%)
            bar = "#" * int(percentage / 5)
            print(f"{category:<20} | ${amount:>9.2f} | {percentage:>5.1f}% {bar}")
        
        print("-" * 50)
        print(f"{'TOTAL':<20} | ${total_spent:>9.2f}")
        print("="*50)