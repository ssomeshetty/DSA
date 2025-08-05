class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if self.root is None:
            self.root = node(key)
            return
        current = self.root
        while current:
            if key < current.key:
                if current.left is None:
                    current.left = node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = node(key)
                    return
                current = current.right
            else:
                return
    
    def search(self,key):
        current = self.root
        while current:
            if current.key == key:
                return True

            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return False

    def inorder(self):
        result = []

        def helper(current):
            if current is None:
                return
            helper(current.left)
            result.append(current.key)
            helper(current.right)

        helper(self.root)

        return result
    def preorder(self):
        result = []
        def helper(current):
            if current is None :
                return 
            result.append(current.key)
            helper(current.left)
            helper(current.right)
        helper(self.root)
        return result
    def postorder(self):
        result = []
        def helper(current):
            if current is None :
                return 
            helper(current.left)
            helper(current.right)
            result.append(current.key)
        helper(self.root)

        return result
    def delete(self, key):
        def delete_node(current, key):
            if current is None:
                return None
            if key < current.key:
                current.left = delete_node(current.left, key)
            elif key > current.key:
                current.right = delete_node(current.right, key)
            else:
                if current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                # Two children
                temp = current.right
                while temp.left:
                    temp = temp.left
                current.key = temp.key
                current.right = delete_node(current.right, temp.key)
            return current
        self.root = delete_node(self.root, key)

    def height(self):
        def helper(node):
            if node is None:
                return -1  # height of empty tree
            left_height = helper(node.left)
            right_height = helper(node.right)
            return 1 + max(left_height, right_height)

        return helper(self.root)

      
bs = bst()
curr = [10,40,30,50,10,50,30,60,2000]

for num in curr:
    bs.insert(num)
    
print(bs.search(400))
print(bs.inorder())
print(bs.preorder())
print(bs.postorder())
bs.delete(40)
print(bs.inorder())
print(bs.preorder())
print(bs.postorder())
print(bs.height())



