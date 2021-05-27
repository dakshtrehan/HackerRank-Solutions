class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
 
        
        
    def getHeight(self, root):
        heightLeft = 0
        heightRight = 0
        if root.left is not None:
            heightLeft = self.getHeight(root.left) + 1
        if root.right is not None:
            heightRight = self.getHeight(root.right) + 1
        return heightLeft if heightLeft > heightRight else heightRight
            
T=int(input())