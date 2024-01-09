def make_withdraw(balance):
	b = [balance]
	def withdraw(amount):
		if amount > b[0]:
			return 'Insufficient funds'
		b[0] -= amount
		return b[0]
	return withdraw