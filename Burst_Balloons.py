class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Approach:
        - Use dynamic programming to solve the problem efficiently.
        - Add 1 at the beginning and end of the nums array to simulate the boundaries.
        - Define a DP table `dp[i][j]` where `i` and `j` represent the range of balloons being considered.
        - `dp[i][j]` will store the maximum coins obtainable by bursting all balloons between indices `i` and `j` (inclusive).
        - For each subarray of balloons, calculate the result by considering each balloon as the last one to burst in that range.
        Time Complexity:
        - O(n^3): The DP table is filled using a nested loop over the range and a loop to choose the last balloon.
        Space Complexity:
        - O(n^2): The DP table requires O(n^2) space.
        """
        # Add 1 to the boundaries for convenience
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Initialize DP table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        # Iterate over the range size
        for length in range(2, n):  # length is the range length
            for left in range(n - length):  # left boundary
                right = left + length  # right boundary
                # Choose the last balloon to burst in the range [left, right]
                for i in range(left + 1, right):
                    # Calculate the coins gained by bursting the ith balloon last
                    coins = nums[left] * nums[i] * nums[right]
                    # Add the coins from bursting balloons in subranges [left, i] and [i, right]
                    dp[left][right] = max(dp[left][right], dp[left][i] + coins + dp[i][right])
        
        # Result is stored in dp[0][n-1], the entire range
        return dp[0][n - 1]
