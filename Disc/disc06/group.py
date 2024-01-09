def group_by(s, fn):
	grouped = {}
	for value in s:
		key = fn(value)
		if key not in grouped:
			grouped[key] = [value]
		else:
			grouped[key].append(value)
	return grouped