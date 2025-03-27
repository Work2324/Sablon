import random
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def append(self, obj):
#         pass


def f(h):
    node = Node(random.randint(1, 10))
    if h > 1:
        node.right = f(h - 1)
        node.left = f(h - 1)
    return node

def pre_order(node):
    if node:
        pre_order(node.left)
        pre_order(node.right)
        print(node.data, end = ' ')

def post_opder(node):
    if node:
        post_opder(node.right)
        post_opder(node.left)
        print(node.data, end = ' ')

def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end = ' ')
        in_order(node.right)


# tree2 = Node(2)
# tree2.left = Node(1)
# tree2.right = Node(3)

tree = f(4)

pre_order(tree)
print()
post_opder(tree)
print()
in_order(tree )



# tree = Node(2)
# tree.left = Node(3)
# tree.right = Node(4)
# tree.left.left = Node(1)
# tree.right.right = Node(5)
# tree.left.left.right = Node(10)