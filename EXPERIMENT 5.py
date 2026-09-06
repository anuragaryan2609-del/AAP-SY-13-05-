#Apply dynamic programming to determine the longest common subsequence between two sequences.

#String 1 = "ABCBDAB"
#String 2 = "BDCAB"

# A.A.	LCS Using Top-Down Approach

def lcs(X, Y, m, n, memo):
    
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if X[m - 1] == Y[n - 1]:
        memo[m][n] = 1 + lcs(X, Y, m - 1, n - 1, memo)

    else:
        memo[m][n] = max(
            lcs(X, Y, m - 1, n, memo),
            lcs(X, Y, m, n - 1, memo)
        )

    return memo[m][n]


X = "ABCBDAB"
Y = "BDCAB"

m = len(X)
n = len(Y)

memo = [[-1] * (n + 1) for _ in range(m + 1)]

print("Length of LCS:", lcs(X, Y, m, n, memo))
#B.	LCS Using Bottom-Up Approach
def lcs(X, Y):

    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


X = "ABCBDAB"
Y = "BDCAB"

print("Length of LCS:", lcs(X, Y))

