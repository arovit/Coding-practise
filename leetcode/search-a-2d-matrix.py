class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not ( matrix and len(matrix[0])) :
            return False
        elif target < matrix[0][0]:
            return False
        elif target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        return self.searchRowColumn(matrix, 0, len(matrix[0])-1, target)
        
    
    def searchRowColumn(self, matrix, row, col, target):
        if col < 0 or row >= len(matrix):
            return False
        elif matrix[row][col] > target:
            return self.searchRowColumn(matrix, row, col-1, target)
        elif matrix[row][col] < target:
            return self.searchRowColumn(matrix, row+1, col, target)
        else:
            return True
        
