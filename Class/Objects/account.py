class Account:
	
	interest = 0.02 # Class attribute

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient fund'
		self.balance -= amount
		return self.balance
