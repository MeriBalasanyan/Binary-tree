# Binary-tree
Trees can be traversed in different ways. The following are generally used ways for traversing trees.
1. Inorder traversal-Traverse the left subtree, then visit the root, and after it traverse the right subtree.
2. Preorder traversal-Visit the root, then traverse the left subtree, and after it traverse the right subtree.
3. Postorder traversal-Traverse the left subtree, then traverse the right subtree, and after it visit the root.
In general time complexity for binry tree traversals is O(n), since we have to visit evey node exactly once. However, if the tree ls 
balanced time complexity is O(log(n)). 
Inorder traversal in the code is 40 20 50 10 30
Preorder traversal in the code is 10 20 40 50 30
Postorder traversal in the code is 40 50 20 30 10
