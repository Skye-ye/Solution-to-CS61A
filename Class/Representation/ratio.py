class Ratio:
	def __init__(self, n, d):
		self.numer = n
		self.denom = d

	def __repr__(self):
		return 'Ration({0}, {1})'.format(self.numer, self.denom)

	def __str__(self):
		return '{0}/{1}'.format(self.numer, self.denom)

	def __add__(self, other):
		if isinstance(other, int):
			n = self.denom * other + self.numer
			d = self.denom
		elif isinstance(other, Ratio):
			n = self.denom * other.numer + self.numer * other.denom
			d = self.denom * other.denom
		elif isinstance(other, float):
			return float(self) + other
		g = gcd(n, d)
		return Ratio(n // g, d // g)

	def __float__(self):
		return self.numer / self.denom

	__radd__ = __add__

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a