def memory(n):
	def f(g):
		nonlocal n
		n = g(n)
		return n
	return f