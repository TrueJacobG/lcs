from .algorithm import Algorithm

# LONGEST COMMON SUBSEQUENCE

class LCSAlgorithm(Algorithm):
    def __init__(self, name: str):
        super().__init__(name)

    # retuns: (length of LCS, LCS string) 
    # complexity: O(x*y) - x and y are lengths of the strings
    def lcs(self, X: str, Y: str) -> tuple[int, str]:
        x, y = len(X), len(Y)
        
        # dp table to store lengths of longest common subsequence
        # we add an extra row and column for the base case (empty string)
        dp = [[0] * (y + 1) for _ in range(x + 1)]
        # x = 2, y = 3
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        
        # filling the dp table
        for i in range(1, x + 1):
            # we are taking first character from X
            # then we compare that with all of the characters from Y
            for j in range(1, y + 1):
                # we are checking all combinations of character from string X and comparing with all characters from string Y
                # if characters are the same, we add 1 to the value from the diagonal cell
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # otherwise we take the maximum value from the left or top cell
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # max lcs length is in the last cell
        # (last row, last column)

        for row in dp:
            print(row)

        # reconstructing the LCS string
        result = []
        i, j = x, y
        
        # we start from the last cell and trace back to the first cell
        while i > 0 and j > 0:
            # if characters are the same, we add it to the result and move diagonally
            if X[i-1] == Y[j-1]:
                result.append(X[i-1])
                i -= 1
                j -= 1
            # otherwise we move in the direction of the larger value
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        # we reverse the result because we traversed the dp table from the end
        result.reverse()
        
        return (dp[x][y], ''.join(result))

def main():
    lcs = LCSAlgorithm("Longest Common Subsequence Algorithm")
    # common subsequence is "BEF"
    X = "ABC"
    Y = "BCD"
    length, subsequence = lcs.lcs(X, Y)

    print("LCS Algorithm Test")
    print(f"Strings - X: {X}, Y: {Y}")
    print(f"Length of LCS is {length}")
    print(f"LCS is {subsequence}")

if __name__ == "__main__":
    main()