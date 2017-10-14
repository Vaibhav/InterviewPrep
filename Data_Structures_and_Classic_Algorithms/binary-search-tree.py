class Tree:
    
    def __init__(self):
        self.root = TreeNode(None, None, None, None)
    
    def is_empty(self):
        if self.root.value is None:
            return True
        else:
            return False
    
    def get_root(self):
        return self.root.value
    
    def add_node(self, val):
        if self.root.value is None:
            self.root.value = val
            return None
        else:
            return self.root.add(val)
    
    def search(self, val):
        return self.root.search(val)
            
class TreeNode:
    
    def __init__(self, parent, left, right, value):
        self.parent = parent
        self.left = left 
        self.right = right
        self.value = value
    
    def add(self, val):
        if self.left is None and self.value > val:
            self.left = TreeNode(self, None, None, val)
            return self.value
        elif self.right is None and self.value < val:
            self.right = TreeNode(self, None, None, val)
            return self.value
        elif self.value > val:
            return self.left.add(val)
        elif self.value < val:
            return self.right.add(val)
        
    def search(self, val):
        if self.value == val:
            return True
        elif self.left is not None and self.value > val:
            return self.left.search(val)
        elif self.right is not None and self.value < val:
            return self.right.search(val)
        return False
    
import unittest

class TestTree(unittest.TestCase):
    def test_empty(self):
        tree = Tree()
        self.assertEqual(tree.is_empty(), True)
        
    def test_root_value(self):
        tree = Tree()
        self.assertEqual(tree.get_root(), None)
        
    def test_add_node(self):
        tree = Tree()
        tree.add_node(5)
        self.assertEqual(tree.is_empty(), False)
        self.assertEqual(tree.get_root(), 5)
    
    def test_add_multiple_nodes(self):
        tree = Tree()
        self.assertEqual(tree.add_node(5), None)
        self.assertEqual(tree.add_node(10), 5)
        self.assertEqual(tree.add_node(15), 10)
        self.assertEqual(tree.add_node(7), 10)
        self.assertEqual(tree.add_node(3), 5)
        self.assertEqual(tree.add_node(2), 3)

        self.assertEqual(tree.search(10), True)
        self.assertEqual(tree.search(4), False)
        

    
unittest.main()
