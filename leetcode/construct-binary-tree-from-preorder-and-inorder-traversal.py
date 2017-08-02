class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.constructTree(preorder, inorder)
        return root
        
    
    def constructTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]       # first node in preorder is root node
        tnode = TreeNode(root_val)   # this is root node 
        rindex = inorder.index(root_val) # find root node index
        
        l_preorder = preorder[:rindex+1][1:] # remain_preorder
        l_inorder = inorder[:rindex]
        tnode.left = self.constructTree(l_preorder, l_inorder)
        
        r_preorder = preorder[rindex+1:]
        r_inorder = inorder[rindex+1:]
        tnode.right = self.constructTree(r_preorder, r_inorder)
        return tnode
