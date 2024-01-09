def merge(a, b):
	next_a = next(a)
	next_b = next(b)
	while(True):
		if next_a is None and next_b is None:
			return
		if next_b is None or (next_a is not None and next_a < next_b):
			yield next_a
			next_a = next(a)
		elif next_a is None or next_a > next_b:
			yield next_b
			next_b = next(b)
		else:
			yield next_a
			next_a = next(a)
			next_b = next(b)
