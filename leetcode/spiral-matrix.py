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
