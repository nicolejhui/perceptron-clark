#def binary search (sorted list (1-1000), num (400)
#   return indec of num
# def BST (root, num)
#   return first node containing num (the one which has lowest height


class Node:

    def __int__(self, value, left, right):
        self.value = value
        self.left = None
        self.right = None
        self.rootnode = None

    def binary_tree_search(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            self.value = value

    def printtree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


# if value is less than root/parent node, then it goes to the left of the parent node

# a = Node()
# a.left = Node() where left is a property of a

# TRASH
#        if numbers[1] < numbers[0]:
#            numbers[0]_node = Node(numbers[0], numbers[1], null)
#        if numbers[1] < numbers[0]:
