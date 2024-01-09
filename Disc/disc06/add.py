def add_this_many(x, el, s):
	helper = s[:]
	for i in helper:
		if i == x:
			s.append(el)
