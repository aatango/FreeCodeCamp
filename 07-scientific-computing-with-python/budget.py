class Category:
	"""
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
		"""Returns the current balance."""

		return self.balance

	def deposit(self, sum: int, desc: str = '') -> None:
		"""Deposits an amount into the category, with an optional description."""

		self.balance += sum
		self.ledger.append({"amount": sum, "description": desc})

	def withdraw(self, sum: int, desc: str = '') -> bool:
		"""If possible, withdraws funds from budget category.

		If the current balance is too low to perform the withdrawal, nothing happens;
		otherwise withdrawal is commited as a deposit of a negative sum.

		ARGS
			sum		amount to withdraw.
			desc	description tag to add to ledger

		RETURNS
			True if there were enough funds in the balance, and withdrawal was performed
		"""

		if self.balance < sum:
			return False
		else:
			self.deposit(-sum, desc)
			return True

	def transfer(self, sum: int, cat: str) -> bool:
		"""If possible, transfers funds from one budget category to another.

		If the withdrawing category doesn't have enough funds for the transfer, nothing happens;
		otherwise, withdrawal is commited to current account,
		and a deposit of the desired budget group is ordered.

		ARGS
			sum amount to transfer between categories.
			cat Category to which funds are to be transferred.

		RETURNS
			True if there where enough funds in the balance, and transfer was performed.
		"""

		if self.balance < sum:
			return False
		else:
			self.ledger.append({"amount": -sum, "description": f"Transfer to {cat.name}"})
			self.balance -= sum
			cat.deposit(sum, f'Transfer from {self.name}')
			return True

	def check_funds(self, sum: int) -> bool:
		"""Checks if argument amount is smaller than the current category balance."""

		return (False if sum > self.balance else True)


def create_spend_chart(categories: list) -> None:
	""" Shows percentage spent in each category.

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
