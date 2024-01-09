def max_product(s):
	if not s:
		return 1

	if len(s) == 1:
		return s[0]

	dp = [0] * len(s)

	dp[0] = s[0]
	dp[1] = max(s[0], s[1])

	for i in range(2, len(s)):
		dp[i] = max(s[i] * dp[i - 2], dp[i - 1])

	return dp[-1]
	