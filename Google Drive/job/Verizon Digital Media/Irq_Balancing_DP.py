class Irq_Balancing_DP:
    # Returns the minimum value of 
    # the difference of the two sets.
    def findMin(self, arr, n):
        """
        :type arr: List[int]
        :type n: int
        """
        # Calculate sum of all elements
        sum = 0
        for i in range(n) :
            sum += arr[i]

        # Create an array to store 
        # results of subproblems
        dp = (n + 1) * [(sum + 1) * [False]]
        #dp = [[False for x in range(n + 1)] for y in range(sum + 1)]
        #dp = [[False for x in range(n + 1)] for y in range(sum + 1)]
        #dp = [n + 1][sum + 1]

        # Initialize first column as true. 
        # 0 sum is possible  with all elements.
        for i in range(n) :
            dp[i][0] = True

        # Initialize top row, except dp[0][0], 
        # as false. With 0 elements, no other 
        # sum except 0 is possible
        for i in range(sum):
            dp[0][i] = False

        # Fill the partition table 
        # in bottom up manner
        for i in range(n):
            for j in range(sum):       
                # If i'th element is excluded
                dp[i][j] = dp[i - 1][j]

                # If i'th element is included
                if arr[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - arr[i - 1]]
            
        # Initialize difference of two sums. 
        #diff = Integer.MAX_VALUE

        # Find the largest j such that dp[n][j]
        # is true where j loops from sum/2 t0 0
        #for j = sum / 2 j >= 0 j-- :
        j = int(sum / 2)
        diff = 0
        while j >= 0 :
            if dp[n][j] == True:
                diff = sum - 2 * j
                break
            j = j - 1

        return diff

    # main function
    def main(self):
        arr = [3, 1, 4, 2, 2, 1, 234]
        n = len(arr)
        print("The minimum difference between 2 sets is "
                + str(self.findMin(arr, n)))

a = Irq_Balancing_DP()
a.main()