class Node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self, depth, value=0):
        self.value = value
        self.left  = BinaryTree(depth-1, value*2 + 1) if depth > 0 \
            else None
        self.right = BinaryTree(depth-1, value*2 + 2) if depth > 0 \
            else None

    def __str__(self, depth=0):
        z = ""

        if self.right != None:
            z += self.right.__str__(depth + 1)

        z += "\n" + ("    "*depth) + str(self.value)

        if self.left != None:
            z += self.left.__str__(depth + 1)

        return z

    def height(self):
        return 1 + max(self.left.height() if self.left is not None else 0,
                       self.right.height() if self.right is not None else 0)

def main():
    print BinaryTree(4)
    print "Height of tree is "

main()
