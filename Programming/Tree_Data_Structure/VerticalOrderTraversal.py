# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    
    def __init__(self):
        # dic: a key valued dictionary list of node values 
        # for each key as distance from root node
        self.dic = {}
        
    
    def VerticalOrderTraversalHelper(self, A, distance, level):
        '''
        @param A: root node of tree
        @param distance: horizontal distance from root node
	@param level: vertical distance from root
        '''
        if A is None:
            return
        if self.dic.get(distance,0):
            self.dic[distance].append([level,A.val])
        else:
            self.dic[distance] = [[level, A.val]]
        
        self.VerticalOrderTraversalHelper(A.left, distance-1, level+1)
        self.VerticalOrderTraversalHelper(A.right, distance+1, level+1)
        
    
    def verticalOrderTraversal(self, A):
        '''
        @param A : root node of tree
        @return a list of list of integers
        '''
        
        self.VerticalOrderTraversalHelper(A,0,0)
        new_arr = []
        for key in sorted(self.dic.keys()):
            new_arr.append([x[1] for x in sorted(self.dic[key], key=lambda x: x[0])])
        
        return new_arr

