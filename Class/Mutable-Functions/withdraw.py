def make_withdraw(balance):
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'Insufficient funds'
		balance -= amount
		return balance
	return withdraw