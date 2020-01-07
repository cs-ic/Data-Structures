s = [1, 2, 6, 3, 7, 4, 9, 8]


class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("Value is already present in BST")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return False

    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        if data == cur_node.data:
            return True


bst = BST()

for i in s:
    bst.insert(i)

print(bst.find(9))
print(bst.find(19))

