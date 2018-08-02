class Irq_Balancing:
    def findMinDiff(self, arr, i, sumCounted, sumTotal):
        """
        :type arr: List[int]
        :type i: int
        :type sumCounted: int
        :type sumTotal: int
        :rtype: int
        """
        if i == 0:
            return abs((sumTotal - sumCounted) -
                       sumCounted);
        return min(self.findMinDiff(arr, i - 1, sumCounted
                                   + arr[i - 1], sumTotal),
                   self.findMinDiff(arr, i - 1,
                                    sumCounted, sumTotal))

    # Returns minimum possible difference between
    # sums of two array arrays
    def findMin(self, arr, n):
        """
        :type arr: List[int]
        :type n: int
        :rtype: int
        """
    # Compute total sum of elements
        sumTotal = 0
        for i in range (n):
            sumTotal += arr[i]
        print ("sumTotal = " + str(sumTotal))
        # Compute result using recursive function
        return self.findMinDiff(arr, n, 0, sumTotal)

    # Driver function to test findMin/findMinDiff functions
    def main(self):
        arr = [3, 1, 4, 2, 2, 1]
        n = len(arr)
        print("The minimum difference"+
                " between two subarrays is " +
                str(self.findMin(arr, n)))

a = Irq_Balancing()
a.main()




