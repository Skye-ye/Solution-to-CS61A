def count_k(n, k):
	dp = [0] * (n + 1)
	dp[0] = 1

	for i in range(1, n + 1):
		for j in range(1, min(i, k) + 1):
			dp[i] += dp[i - j]

	return dp[n]