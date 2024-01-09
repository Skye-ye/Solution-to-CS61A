def even_weighted(s):
	return [s[i] * i for i in range(len(s)) if i % 2 == 0]