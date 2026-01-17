class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""

        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:>7.2f}"
            body += f"{desc:<23}{amount}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + body + total



    def create_spend_chart(categories):
        spent = []

        for category in categories:
            total = 0
            for item in category.ledger:
                if item["amount"] < 0:
                    total += -item["amount"]
            spent.append(total)

        total_spent = sum(spent)
        percentages = [(s/ total_spent) * 100 for s in spent]
        percentages = [int(p // 10) * 10 for p in percentages]

        chart = "Percentage spent by category\n"

        for level in range(100, -1, -10):
            chart += f"{level:>3}|"
            for p in percentages:
                chart += " o " if p >= level else "   "
            chart += " \n"

        chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

        max_len = max(len(c.name) for c in categories)
        for i in range(max_len):
            chart += "     "
            for c in categories:
                chart += f"{c.name[i]}  " if i < len(c.name) else "   "
            chart += "\n"

        return chart.rstrip("\n")