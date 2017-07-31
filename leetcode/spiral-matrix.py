class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        elif len(matrix[0]) == 1:
            return [k[0] for k in matrix]
        self.done = {}
        resultant = []
        self.spiralFirstLast(matrix, len(matrix), len(matrix[0]), 0, resultant)
        return resultant
        
    def spiralFirstLast(self, matrix, totrows, totcols, layer, spiralResult):
        print "layer %s result %s"%(layer, spiralResult)
        if len(spiralResult) >= totrows*totcols:
            return 
        spiralResult.extend(matrix[layer][layer:totcols-layer])
        for i in range(layer+1, totrows-layer-1):
            if (i,totcols-layer-1) not in self.done:
                spiralResult.append(matrix[i][totcols-layer-1])
                self.done[(i,totcols-layer-1)] = 1
        if layer != totrows-layer-1:
            spiralResult.extend(matrix[totrows-layer-1][layer:totcols-layer][::-1])
        for i in range(totrows-layer-2, layer, -1):
            if (i,layer) not in self.done:
                spiralResult.append(matrix[i][layer])
                self.done[(i,layer)] = 1
        self.spiralFirstLast(matrix, totrows, totcols, layer + 1, spiralResult


# BEST SOLUTION

    class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            if not matrix:
                return matrix
            solution = []        # solution array
            state = 1
            minRow = minCol = 0  # lower boundries of rows/col
            maxRow = len(matrix) - 1
            maxCol = len(matrix[0]) -1
            i = j = 0
            if j == maxCol:
                state = 2
            while len(solution) < (len(matrix) * len(matrix[0])): # if solution is not full
                solution.append(matrix[i][j])
                if state == 1:  # first row traversal
                    if j == maxCol:  # if maxCol is reached
                        state = 2
                        minRow += 1  # reduct minRow
                        i += 1
                    else:
                        j += 1
                elif state == 2:  # last row downward traversal
                    if i == maxRow:
                        state = 3
                        maxCol -= 1
                        j -= 1
                    else:
                        i += 1
                elif state == 3:  # last row rev travrsal
                    if j == minCol:
                        state = 4
                        maxRow -= 1
                        i -= 1
                    else:
                        j -= 1
                elif state == 4:  # last col upper traversal
                    if i == minRow:
                        state = 1
                        minCol += 1
                        j += 1
                    else:
                        i -= 1
            return solution
