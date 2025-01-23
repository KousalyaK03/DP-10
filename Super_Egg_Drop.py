class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        Approach:
        - Use dynamic programming to solve the problem efficiently.
        - Let dp[m][k] represent the maximum number of floors that can be tested with k eggs and m moves.
        - Base Cases:
          - dp[0][k] = 0 (0 floors can be tested with 0 moves).
          - dp[m][0] = 0 (0 floors can be tested with 0 eggs).
        - Transition:
          - dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1
          - If we drop an egg from a floor:
            - If it breaks: Use m-1 moves and k-1 eggs to test below the floor.
            - If it doesn’t break: Use m-1 moves and k eggs to test above the floor.
        - The goal is to find the minimum number of moves (m) such that dp[m][k] >= n.
        Time Complexity:
        - O(k * log(n)): The loop runs until the number of moves (m) is sufficient to test all n floors.

        Space Complexity:
        - O(k): We only keep track of the previous states in a 1D array.
        """

        # DP array for storing states for each move
        dp = [0] * (k + 1)
        moves = 0

        # Continue until we can test at least `n` floors
        while dp[k] < n:
            moves += 1
            # Update dp array for the current move
            for i in range(k, 0, -1):
                dp[i] = dp[i - 1] + dp[i] + 1

        return moves
