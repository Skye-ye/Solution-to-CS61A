def plus_minus(x):
	yield x
	yield -x

def evens(start, end):
	even = start + start % 2
	while even < end:
		yield even
		even += 2

def a_then_b(a, b):
	yield from a
	yield from b

def count_down(k):
	if k > 0:
		yield k
		yield from count_down(k - 1)
	else:
		yield 'Blast off'

def prefixes(s):
	if s:
		yield from prefixes(s[:-1])
		yield s

def substrings(s):
	if s:
		yield from prefixes(s)
		yield from substrings(s[:-1])