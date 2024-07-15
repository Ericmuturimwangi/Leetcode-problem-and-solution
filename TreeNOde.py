class TreeNode:
    
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        self.content = None


    def insert(self, value, content=None):
        # alg is simple: if a value is less than the par we go left otherwise we go right
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
            
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None

            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self


tree = TreeNode(10)
tree.insert(5)
tree.insert(11)
tree.insert(1)
tree.insert(6)
tree.insert(2, {"data":"Hello WOrld"})
tree.insert(4)

print(tree.find(2).content['data'])



