"""def filter(iterable, fn):
	for x in iterable:
		if fn(x):
			yield x
"""

def filter(iterable, fn):
    return (x for x in iterable if fn(x))