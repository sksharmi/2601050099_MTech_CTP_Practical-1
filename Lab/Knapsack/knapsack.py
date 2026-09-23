def knapsack(wt, val, W):
    dp = [0] * (W + 1)

    for i in range(len(wt)):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]

wt = [1, 3, 4]
val = [15, 20, 30]
W = 4

print("Maximum value:", knapsack(wt, val, W))