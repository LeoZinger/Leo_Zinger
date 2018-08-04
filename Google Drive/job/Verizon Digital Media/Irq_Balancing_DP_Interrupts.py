import csv
class Irq_Balancing:
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
        # print ("After initing 2D DP array ALL False:" + str(dp))

        # Initialize first column as true.
        # 0 sum is possible  with all elements.
        # for i in range(0, n+1, 1):
        # for i in range(n+1) :
        i = 0
        while i <= n :
            dp[i][0] = True
            i += 1
        # print ("After setting 1st column to True : " + str(dp))

        # Initialize top row, except dp[0][0],
        # as false. With 0 elements, no other
        # sum except 0 is possible
        i = 1
        while i <= sum :
            dp[0][i] = False
            i += 1
        # print ("After setting top row to False :   " + str(dp))

        # Fill the partition table
        # in bottom up manner
        print ("n = " + str(n))
        for i in range(1, n+1):
            for j in range(1, sum+1):
                # If i'th element is excluded
                dp[i][j] = dp[i - 1][j]
                # print("After " + str(i) + "'th element excluded :" + str(dp))

                # If i'th element is included
                if arr[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - arr[i - 1]]
                    # if (dp[i - 1][j - arr[i - 1]] == True) or (dp[i][j] == True):
                    #     dp[i][j] = True

            #     print("inner loop sum, j = " + str(j))
            # print("outer loop n, i = " + str(i))

        # print ("After Filling the partition table :" + str(dp))

        # Initialize difference of two sums.
        #diff = Integer.MAX_VALUE
        #diff = 1000000000

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

    # Returns minimum difference between
    # sums of two array arrays
    # def findMin(self, arr, n):
    #     """
    #     :type arr: List[int]
    #     :type n: int
    #     :rtype: int
    #     """
    # # Compute total sum of elements
    #     sumTotal = 0
    #     res_arr = []
    #     for i in range (n):
    #         sumTotal += arr[i]
    #     print ("sumTotal = " + str(sumTotal))
    #     # Compute result using recursive function
    #     minDiff, res_arr = self.findMinDiff(arr, n-1, 0, sumTotal, [])
    #     print ("findMin:" + str(res_arr))
    #     return minDiff, res_arr

    # main function to test findMin/findMinDiff functions
    def main(self, irq_list):
        arr = irq_list
        # arr = [8, 1, 7, 3, 4, 2, 250]
        # arr = [ 5, 1, 3, 4, 2, 2, 8]
        res_countedIndexArr = [0 for x in range(len(arr))]
        print ("arr length = " + str(len(arr)))
        print ("res_countedIndexArr size = " + str(len(res_countedIndexArr)))
        n = len(arr)
        # (minDiff, res_countedIndexArr) = self.findMin(arr, n)
        minDiff = self.findMin(arr, n)
        print("The minimum difference between two subarrays is " +
            str(minDiff))

        print("The result array indices : " + str(res_countedIndexArr))

    def get_irq_list_from_file(self, filename):
        irq_list = []
        for line in open(filename):
            listWords = line.split()
            irq_list.append(int(listWords[1]) + int(listWords[2]))
            print (listWords[0] + " " + str(int(listWords[1]) + int(listWords[2])))

        print (str(irq_list))
        return irq_list

a = Irq_Balancing()
irq_list = a.get_irq_list_from_file("C:\\Users\Leo_Zinger\Downloads\Irq_Balancing\irq_interrupts.txt")
a.main(irq_list)
