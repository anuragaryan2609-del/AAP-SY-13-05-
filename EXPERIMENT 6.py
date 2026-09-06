#Apply dynamic programming techniques for optimal selection of items to maximize value within a weight constraint using bottom-up and top-down approaches. 
#A. 0/1 Knapsack Using Top-Down DP
def knapsack(W, weights, values, n, memo):

    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1:
        return memo[n][W]

    if weights[n - 1] > W:

        memo[n][W] = knapsack(
            W,
            weights,
            values,
            n - 1,
            memo
        )

    else:

        include = values[n - 1] + knapsack(
            W - weights[n - 1],
            weights,
            values,
            n - 1,
            memo
        )

        exclude = knapsack(
            W,
            weights,
            values,
            n - 1,
            memo
        )

        memo[n][W] = max(include, exclude)

    return memo[n][W]


values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]

W = 5
n = len(values)

memo = [[-1] * (W + 1) for _ in range(n + 1)]

print("Maximum Value:",
      knapsack(W, weights, values, n, memo))


#B. 0/1 Knapsack Using Bottom-Up DP
def knapsack(W, weights, values):

    n = len(values)

    dp = [[0] * (W + 1)
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(1, W + 1):

            if weights[i - 1] <= w:

                include = values[i - 1] + \
                          dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]

W = 5

print("Maximum Value:",
      knapsack(W, weights, values))

