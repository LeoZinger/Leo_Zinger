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
        print ("arr sum = " + str(sum))
        # Create an array to store 
        # results of subproblems
        #dp = [n + 1][sum + 1]
        dp = [[False for x in range(sum+1)] for y in range(n+1)]
        print ("After initing 2D DP array ALL False:" + str(dp))
        # dp = (n + 1) * [(sum + 1) * [False]]
        # print (str(dp))

        # Initialize first column as true. 
        # 0 sum is possible  with all elements.
        # for i in range(0, n+1, 1):
        # for i in range(n+1) :
        i = 0
        while i <= n :
            dp[i][0] = True
            i += 1
        print ("After setting 1st column to True : " + str(dp))

        # Initialize top row, except dp[0][0], 
        # as false. With 0 elements, no other 
        # sum except 0 is possible
        i = 1
        while i <= sum :
            dp[0][i] = False
            i += 1
        print ("After setting top row to False :   " + str(dp))

        # Fill the partition table 
        # in bottom up manner
        i = 1
        j = 1
        # for i in range(1, n+1):
        while i <= n :
            # for j in range(1, sum+1):
            while j <= sum :
                # If i'th element is excluded
                dp[i][j] = dp[i - 1][j]

                # If i'th element is included
                if arr[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - arr[i - 1]]
                    # if (dp[i - 1][j - arr[i - 1]] == True) or (dp[i][j] == True):
                    #     dp[i][j] = True

                j += 1
            i += 1

        print ("After Filling the partition table :" + str(dp))

        # Initialize difference of two sums.
        #diff = Integer.MAX_VALUE
        diff = 1000000000

        # Find the largest j such that dp[n][j]
        # is True where j loops from sum/2 to 0
        #for j = sum / 2 j >= 0 j-- :
        j = int(sum / 2)
        print ("sum/2 = " + str(j))
        while j >= 0 :
            if dp[n][j] == True:
                diff = sum - j * 2
                break
            j -= 1

        return diff

    # main function
    def main(self):
        arr = [3, 1, 4, 2, 2, 1]
        n = len(arr)
        print("The minimum difference between 2 sets is "
                + str(self.findMin(arr, n)))

a = Irq_Balancing_DP()
a.main()