'''
array vesion of Segment Tree will give MLE because there are a LOT of dummy/blank array cells assigned
-using TreeNodes is better because it takes less space and is more efficient for SPARSE (aka not full) binary trees
-but using an array is easier to construct?? maybe-ish?

-first create a dummy root node
    root = TreeNode()
-then create the segment tree from that root
    segTree = root.build(arr, 0, len(arr)-1)

'''
class TreeNode:
    def __init__(self, start=0, end=0):
        self.sum = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
    def build(self, nums, start, end):
        if start > end: #base case
            return None
        elif start == end: #leaf node
            leaf = TreeNode(start, end) #creating a treeNode obj, calling its own constructor lol
            leaf.sum = nums[start]
            return leaf

        mid = start + (end - start) // 2
        node = TreeNode(start, end)

        node.left = self.build(nums, start, mid)
        node.right = self.build(nums, mid+1, end)
        node.sum = node.left.sum + node.right.sum
        return node
    
    def update(self, node, idx, val):
        if node.start == node.end: #that means the interval is len 1, so its a leaf
            node.sum = val
            return
        
        mid = node.start + (node.end - node.start) // 2
        
        if idx <= mid:
            self.update(node.left, idx, val)
        else:
            self.update(node.right, idx, val)
        
        node.sum = node.left.sum + node.right.sum
    
    def sumRange(self, node, start, end):
        if node.start == start and node.end == end:
            return node.sum
        
        mid = node.start + (node.end - node.start)//2

        if end <= mid:
            return self.sumRange(node.left, start, end)
        elif start > mid:
            return self.sumRange(node.right, start, end)
        else:
            return self.sumRange(node.left, start, mid) + self.sumRange(node.right, mid+1, end)
        
    def dfs(self, node): #for testing purposes
        if not node:
            return
        self.dfs(node.left)
        self.dfs(node.right)