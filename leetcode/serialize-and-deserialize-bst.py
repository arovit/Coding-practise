#!/usr/bin/python


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder_list = []
        if root: 
            self.do_preorder(root, preorder_list)           
        return str(preorder_list)
        
    def do_preorder(self, node, plist):
        """ Do preorder traversal """
        plist.append(node.val)
        if node.left:
            self.do_preorder(node.left, plist)
        if node.right:
            self.do_preorder(node.right, plist)
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = []
        preorder_list = eval(data)
        if preorder_list:
            root = self.form_tree(preorder_list)
        return root
        
    def getPartitionIndex(self, preorder_list, cvalue):
        pindex = len(preorder_list)
        for index, value in enumerate(preorder_list):
            if value > cvalue:
                pindex = index
                break
        return preorder_list[:pindex], preorder_list[pindex:]
              
    def form_tree(self, preorder_list):
        rnode = TreeNode(preorder_list[0])   # first one is always root node
        larray, rarray = self.getPartitionIndex(preorder_list[1:], rnode.val)
        if larray:
            rnode.left = self.form_tree(larray)
        if rarray:
            rnode.right = self.form_tree(rarray)
        return rnode
