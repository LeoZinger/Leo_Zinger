import csv
class Irq_Balancing:
    def findMinDiff(self, arr, i, sumCounted, sumTotal, countedIndexArr):
        """
        :type arr: List[int]
        :type i: int
        :type sumCounted: int
        :type sumTotal: int
        :type countedIndexArr: List[int]
        """
        if not countedIndexArr:
            #print("List countedIndexArr is empty")
            newCountedIndexArr = [i]
        else:
            newCountedIndexArr = countedIndexArr.copy()
            newCountedIndexArr.append(i)
            #print(newCountedIndexArr)

        if i == 0:
            return abs((sumTotal - sumCounted) -
                       sumCounted), countedIndexArr

        min_include_current, ret_include_countedIndexArr = self.findMinDiff(arr, i - 1, sumCounted
                                               + arr[i - 1], sumTotal, newCountedIndexArr)
        min_not_include_current, ret_not_include_countedIndexArr = self.findMinDiff(arr, i - 1,
                                                   sumCounted, sumTotal, countedIndexArr)
        if min_include_current < min_not_include_current :
            # add index in the result array
            #print (i)
            countedIndexArr = newCountedIndexArr
            print ("returned included indexArray:" + str(ret_include_countedIndexArr))
            return min_include_current, ret_include_countedIndexArr
        else:
            print ("returned NOT-included indexArray:" + str(ret_not_include_countedIndexArr))
            return min_not_include_current, ret_not_include_countedIndexArr

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
        res_arr = []
        for i in range (n):
            sumTotal += arr[i]
        print ("sumTotal = " + str(sumTotal))
        # Compute result using recursive function
        minDiff, res_arr = self.findMinDiff(arr, n-1, 0, sumTotal, [])
        print ("findMin:" + str(res_arr))
        return minDiff, res_arr

    # Driver function to test findMin/findMinDiff functions
    def main(self):
        arr = [8, 1, 7, 3, 4, 2, 250]
        #arr = [ 5, 1, 3, 4, 2, 2, 1]
        res_countedIndexArr = [0 for x in range(len(arr))]
        #res_countedIndexArr = []
        #res_countedIndexArr = [len(arr)+1];
        print ("arr length = " + str(len(arr)))
        print ("res_countedIndexArr size = " + str(len(res_countedIndexArr)))
        n = len(arr)
        (minDiff, res_countedIndexArr) = self.findMin(arr, n)
        print("The minimum difference"+
                " between two subarrays is " +
                str(minDiff))

        #print("The result array for one of the subarrays : " +
        #  str(res_countedIndexArr))

        print("The result array indices : " + str(res_countedIndexArr))

        # for index in range(len(res_countedIndexArr)):
        # #for i in res_countedIndexArr:
        #     if res_countedIndexArr[index] >= 1:
        #         print(str(index))

    def read_irq_file(self, filename):
        for line in open(filename):
            listWords = line.split()
            #print (listWords[0] + " " + listWords[1] + " " + listWords[2])
            #irq_arr =
            print (listWords[0] + " " + str(int(listWords[1]) + int(listWords[2])))


a = Irq_Balancing()
#a.read_irq_file("C:\\Users\Leo_Zinger\Downloads\Irq_Balancing\irq_interrupts.txt")
a.main()




