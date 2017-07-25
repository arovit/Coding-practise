#!/usr/bin/python

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        h = self.getHeight(root)
        list_repr = [[] for i in range(h)]
        self.levelInsert(list_repr, 0, root, h)
        data = '%s'%list_repr
        print data
        return data
        
        
    def levelInsert(self, list_repr, level, node, height):
        if level == height:
            return 
        sval = None if not node else node.val
        list_repr[level].append(sval)
        self.levelInsert(list_repr, level+1, None if not node else node.left, height)
        self.levelInsert(list_repr, level+1, None if not node else node.right, height)
        
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        list_repr = eval(data)
        root = self.constructTree(list_repr, 0, 0)
        return root
            
            
    def constructTree(self, list_repr, level, index):
        if level == len(list_repr):
            return None
        val = list_repr[level][index]  # get the value
        if val is not None:
            node = TreeNode(val)       # convert value into Node
            node.left = self.constructTree(list_repr, level+1, 2*index)
            node.right = self.constructTree(list_repr, level+1, 2*index + 1)
            return node
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
