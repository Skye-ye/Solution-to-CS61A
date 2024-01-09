def count_stair_ways(n):
	if n == 0 or n == 1:
		return 1
	else:
		return count_stair_ways(n - 1) + count_stair_ways(n - 2)