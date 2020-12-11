###### tags: `Data_Structure`

# Tree


![](https://i.imgur.com/8xHLgd5.png)
Q's indegree is 1
Q's outdegree is 2


## General Tree
A general tree is a tree data structure where there are no constraints on the hierarchical structure.

**Properties**
1. Follow properties of a tree.
2. A node can have any number of children.

![](https://i.imgur.com/ZqqhVQo.png)


**Usage**
1. Used to store hierarchical data such as folder structures.

## Binary Tree

A binary tree is a tree data structure where the following properties can be found.

**Properties**
1. Follow properties of a tree.
2. A node can have at most two child nodes (children).
3. These two child nodes are known as the left child and right child.

![](https://i.imgur.com/ve55Ik9.png)

**Usage**
1. Used by compilers to build syntax trees.
2. Used to implement expression parsers and expression solvers.
3. Used to store router-tables in router.

## Binary Search Tree
A binary search tree is a more constricted extension of a binary tree.

**Properties**

1. Follow properties of a binary tree.
2. Has a unique property known as the binary-search-tree property. This property states that the value (or key) of the left child of a given node should be less than or equal to the parent value and the value of the right child should be greater than or equal to the parent value.

![](https://i.imgur.com/hideg1x.png)


**Usage**
1. Used to implement simple sorting algorithms.
2. Can be used as priority queues.
3. Used in many search applications where data are constantly entering and leaving.

## AVL tree

An AVL tree is a self-balancing binary search tree. This is the first tree introduced which automatically balances its height.

**Properties**
1. Follow properties of binary search trees.
2. Self-balancing.
3. Each node stores a value called a balance factor which is the difference in height between its left subtree and right subtree.
4. All the nodes must have a balance factor of -1, 0 or 1.

After performing insertions or deletions, if there is at least one node that does not have a balance factor of -1, 0 or 1 then rotations should be performed to balance the tree (self-balancing). You can read more about the rotation operations in my previous article from here.

![](https://i.imgur.com/2tDltQA.png)

## Red-black tree
A red-black tree is a self-balancing binary search tree, where each node has a colour; red or black. The colours of the nodes are used to make sure that the tree remains approximately balanced during insertions and deletions.
**Properties**

1. Follow properties of binary search trees.
2. Self-balancing.
3. Each node is either red or black.
4. The root is black (sometimes omitted).
5. All leaves (denoted as NIL) are black.
6. If a node is red, then both its children are black.
7. Every path from a given node to any of its leaf nodes must go through the same number of black nodes.


![](https://i.imgur.com/FCAY7Hf.png)


**Usage**
1. As a base for data structures used in computational geometry.
2. Used in the Completely Fair Scheduler used in current Linux kernels.
3. Used in the epoll system call implementation of Linux kernel.

## Splay tree
A splay tree is a self-balancing binary search tree.
**Properties**
1. Follow properties of binary search trees.
2. Self-balancing.
3. Recently accessed elements are quick to access again.

After performing a search, insertion or deletion, splay trees perform an action called splaying where the tree is rearranged (using rotations) so that the particular element is placed at the root of the tree.

![](https://i.imgur.com/nVjJMEf.png)

**Usage**
1. Used to implement caches
2. Used in garbage collectors.
3. Used in data compression

## Treap
A treap (the name derived from tree + heap) is a binary search tree.
**Properties**
1. Each node has two values; a key and a priority.
2. The keys follow the binary-search-tree property.
3. The priorities (which are random values) follow the heap property.

![](https://i.imgur.com/1A6O4lN.png)

**Usage**
1. Used to maintain authorization certificates in public-key cryptosystems.
2. Can be used to perform fast set operations.

## B-tree
B tree is a self-balancing search tree and contains multiple nodes which keep data in sorted order. Each node has 2 or more children and consists of multiple keys.

**Properties**

1. Every node x has the following:

	1. x.n (the number of keys)
	2. x.keyᵢ (the keys stored in ascending order)
	3. x.leaf (whether x is a leaf or not)

2. Every node x has (x.n + 1) children.

3. The keys x.keyᵢ separate the ranges of keys stored in each sub-tree.

4. All the leaves have the same depth, which is the tree height.

5. Nodes have lower and upper bounds on the number of keys that can be stored. Here we consider a value t>=2, called minimum degree (or branching factor) of the B tree.

	1. The root must have at least one key.

	2. Every other node must have at least (t-1) keys and at most (2t-1) keys. Hence, every node will have at least t children and at most 2t children. We say the node is full if it has (2t-1) keys.

![](https://i.imgur.com/itYxWeT.png)

**Usage**
1. Used in database indexing to speed up the search.
2. Used in file systems to implement directories.
