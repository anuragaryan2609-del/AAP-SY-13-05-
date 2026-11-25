# Items: weights and values
weights = [1, 3, 4, 5]
values = [2, 6, 8, 9]
capacity = 8


# -------------------------------
#  Bottom-Up Approach
# -------------------------------
def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# -------------------------------
#  Top-Down Approach
# -------------------------------
def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, w):
        if i == 0 or w == 0:
            return 0

        if (i, w) in memo:
            return memo[(i, w)]

        if weights[i - 1] <= w:
            memo[(i, w)] = max(
                values[i - 1] + solve(i - 1, w - weights[i - 1]),
                solve(i - 1, w)
            )
        else:
            memo[(i, w)] = solve(i - 1, w)

        return memo[(i, w)]

    return solve(n, capacity)


# Display results
print("Maximum value using Bottom-Up:", 
      knapsack_bottom_up(weights, values, capacity))

print("Maximum value using Top-Down:", 
      knapsack_top_down(weights, values, capacity))
