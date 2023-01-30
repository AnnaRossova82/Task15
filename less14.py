from binarytree import Node
from binarytree import *
import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
      self.root = None
      self.size = 0

    def __iter__(self):
      return self.root.__iter__()

    def __find(self, node, parent, value):
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find = self.__find(self.root, None, obj.data)

        def test_matching(self):
            self.assertFalse(self.root == None, "No root found")
            self.assertTrue(self.root == self.obj, "Success")

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
            return obj

    def check_vis(self, node):
        if node is None:
            return

        self.check_vis(node.left)
        print(node.data)
        self.check_vis(node.right)

    def __find_min(self, node):
        if node.left:
            return self.__find_min(node.left)

    def __find_max(self, node):
        if node.right:
            return self.__find_max(node.right)

        def test_find_max():
            assert self.__find_max(node.right)

    def del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def test_del_leaf(self):
        self.assertEqual((self.del_leaf.s, self.del_leaf.p), None, None)

    def __del_one_child(self, s, p):
        if p.left ==s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.right is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        if s.right is None and s.left is None:
            self.__del_leaf(s, p)
        elif s.right is None or s.left is None:
            self.__del_one_child(s, p)

v = [15, 8, 7, 19, 14, 1, 26]

t = Tree()
for x in v:
    t.append(Node(x))
t.check_vis(t.root)

test_find_max()
test_matching()
test_del_leaf()

#@pytest.parametrize("a, expected_result", [(5, True),
#                                            (4, False)])
#def test_del_leaf(a, b, expected_result):
#    assert a + b == 37

def test_always_passes():
    assert True