class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # idea is to do level wise and reverse every alternate
        if not root:
            return []
        #tmp = root
        h = self.getHeight(root)
        levelWise = [[] for i in range(h)]
        self.levelWisePrint(levelWise, root, 0)
        for i in range(1,h,2):
            levelWise[i] = levelWise[i][::-1]
        return levelWise
 
    def getHeight(self, node):
        if not node:
            return 0
        l = r = 0
        if node.left:
            l = self.getHeight(node.left)
        if node.right:
            r = self.getHeight(node.right)
        return max(l,r)+1
     
    def levelWisePrint(self, levelWise, node, index):
        levelWise[index].append(node.val)
        if node.left:
            self.levelWisePrint(levelWise, node.left, index+1)
        if node.right:
            self.levelWisePrint(levelWise, node.right, index+1)
        
