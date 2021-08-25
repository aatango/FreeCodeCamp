class Category:
	"""Category is able to instantiate objects based on
	different budget categories (like food, clothing, and entertainment).

	When objects are created, they are passed in the name of the category.
	Class has instance variable called ledger as a list.
	"""

	def __init__(self, name: str) -> None:
		self.balance = 0
		self.ledger = []
		self.name = name

	def __str__(self) -> str:
		summary = self.name.center(30, '*') + '\n'
		for i in range(len(self.ledger)):
			summary += (f'{self.ledger[i]["description"]}'[:23].ljust(23)
				+ f'{"{:,.2f}".format(self.ledger[i]["amount"])}'[:7].rjust(7)
				+ '\n'
			)
		summary += f'Total: {self.balance}'
		return summary

	def get_balance(self) -> int:
		"""Returns the current balance based on past deposits and withdrawals."""

		return self.balance

	def deposit(self, sum: int, desc: str = '') -> None:
		"""Deposits an amount into the category, with an optional description.
		
		If no description is given, it defaults to an empty string.
		"""

		self.balance += sum
		self.ledger.append({"amount": sum, "description": desc})

	def withdraw(self, sum: int, desc: str = '') -> bool:
		"""If possible, withdraws funds from budget category.

		Similar to deposit method, but ammount passed in is stored
		in the ledger as a negative number.

		If the current balance is too low to perform the withdrawal,
		nothing happens; otherwise withdrawal is commited
		 as a deposit of a negative sum.

		ARGS
		sum		amount to withdraw.
		desc	description tag to add to ledger

		RETURNS
		True if there were enough funds in the balance,
		and withdrawal was performed
		"""

		if self.balance < sum:
			return False
		else:
			self.deposit(-sum, desc)
			return True

	def transfer(self, sum: int, cat: str) -> bool:
		"""If possible, transfers funds from one budget category to another.

		Accepts amount and another budget category as arguments.

		Adds withdrawal with the amount and description
		"Transfer to [Destination Budget Category].

		Then adds deposit to other budget category with amount,
		and description "Transfer from [Source Budget Category].

		If there are not enough funds,nothing is to be added to either ledgers.

		ARGS
		sum amount to transfer between categories.
		cat Category to which funds are to be transferred.

		RETURNS
		True if there where enough funds in the balance,
		and transfer was performed.
		"""

		if self.balance < sum:
			return False
		else:
			self.ledger.append(
				{"amount": -sum, "description": f"Transfer to {cat.name}"}
			)
			self.balance -= sum
			cat.deposit(sum, f'Transfer from {self.name}')
			return True

	def check_funds(self, sum: int) -> bool:
		"""Checks if argument amount is smaller than the current category balance.
		
		Method can be used by both the withdraw and transfer methods.
		"""

		return (False if sum > self.balance else True)


def create_spend_chart(categories: list) -> str:
	"""Returns bar chart as string

	Chart shows the percentage spent in each category passed in to the function.
	Percentage spent is calculated only with withdrawals, and not with deposits.

	Down the left side are labels 0 - 100.
	The "bars" in the bar chart are made out of the "o" character.
	The height of each bar is rounded down to the nearest 10.
	Horizontal line below the bars goes two spaces past the final bar.
	Each category name is written vertically below the bar,

	There is a title at the top: "Percentage spent by category"

	ARGS
	categories	Items which to evaluate
	"""

	# Expenses inc. total
	expenses = []
	for category in categories:
		cat_expense = 0
		for entry in category.ledger:
			if entry["amount"] < 0:
				cat_expense += entry["amount"]
		expenses.append(cat_expense)
	sum_expenses = sum(expenses)
	cat_expenses = [(i / sum_expenses) * 10 // 1 * 10 for i in expenses]

	# Category names
	cat_names = [cat.name for cat in categories]
	max_name_length = max(len(i) for i in cat_names)
	cat_names = [cat.name.ljust(max_name_length) for cat in categories]

	# String formatting
	summary = ['Percentage spent by category']
	for i in range(100, 0, -10):
		ticks = ''
		for expense in cat_expenses:
			ticks += ('o'*bool(expense // (i - 1))).ljust(3)
		summary.append(f'{i}'.rjust(3) + '| ' + ticks)
	summary.append('  0| ' + 'o  '*len(categories))
	summary.append('    -' + '-' * 3 * len(categories))
	naming = []
	for i in range(max_name_length):
		name_list = ''
		for char in cat_names:
			name_list += f'{char[i]}  '
		naming.append('     ' + name_list)
	summary.extend(naming)

	return '\n'.join(summary)
