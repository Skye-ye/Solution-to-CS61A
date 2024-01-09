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

class CheckingAccount(Account):
	withdraw_fee = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
	# A bank *has* accounts

	def __init__(self):
		self.accounts = []

	def open_account(self, holder, amount, kind=Account):
		account = kind(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		for a in self.accounts:
			a.deposit(a.balance * a.interest)

	def too_big_to_fail(self):
		return len(self.accounts) > 1

class SavingAccount(Account):
	deposit_fee = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 1














