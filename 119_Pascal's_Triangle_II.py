class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        temp = [1]
        rowIndex = rowIndex + 1
        for i in range(rowIndex):
        	
        	theRow = []

        	for j in range(i+1):
        		if j == 0 or j == len(temp):
        			theRow.append(1)
        		else:
        			theRow.append(temp[j-1] + temp[j])
        	temp = theRow
#        print theRow

        return theRow

#    getRow(object, 3)
    def getRow2(self, rowIndex):
		row = [1]
		for _ in range(rowIndex):
			row = [x + y for x, y in zip([0] + row, row + [0])]
			

			print row
		return row
    #getRow2(object, 3)

#if __name__ == "__main__":
print Solution().getRow2(3)