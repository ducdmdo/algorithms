/* Binary Search Tree */

	// Node class - to represent a node object which included node's data, left object and right object
	class Node {
		constructor(data, left = null, right = null) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}

	// BST class - to represent Binary Search Tree object; in a Binary Search Tree - we only need to manage the root node
	class BST {
		constructor() {
			this.root = null;
		}

		//add method - to add a node to the Binary Search Tree
		add(data) {
			let node = this.root;
			if (node === null) { 
				this.root = new Node(data);
				return;
			}else {
				let searchTree = function(node) {
					if (data <= node.data) {
						if (node.left === null) {
							node.left = new Node(data);
							return;
						} else if (node.left !== null) {
							return searchTree(node.left);
						}
					} else if (data > node.data) {
						if (node.right === null) {
							node.right = new Node(data);
							return;
						} else if (node.right !== null) {
							return searchTree(node.right);
						}
					} else {
						return null;
					}
				}
				return searchTree(node);
			}
	
		}

		// findMin method - return the smallest item in the tree
		findMin() {
			let current = this.root;
			while (current.left !== null) {
				current = current.left;
			}
			return current.data;
		}

		// findMax method - return the largest item in the tree
		findMax() {
			let current = this.root;
			while (current.right !== null) {
				current = current.right;
			}
			return current.data;
		}

		// find method - check whether existing item in the tree
		find (data) {
			let current = this.root;

			if (current.data === data) {
				return current.data;
			} else {
					while (current.data !== data) {
						if (current.data < data) {
							current = current.left
						} else {
							current = current.right
						}
						if (current === null) {
							return null;
						}
					}
				return current;
			}
		}

		// isPresent method - check whether item is existing in the tree
		isPresent(data) {
			let current = this.root;
			while (current) {
				if (data === current.data) {
					return true;
				}
				if (data < current.data) {
					current = current.left;
				} else {
					current = current.right;
				}
			}
			return false;
		}

		// remove method - remove an desired item in the tree
		remove (data) {
			const removeNode = function(node, data) { 
				if (node == null) {
					return null;
				}
				if (data == node.data) {
					// remove the node which has no children
					if (node.left == null && node.right == null) {
						return null;
					}
					// node has no left child
					if (node.left == null) {
						return node.right;
					}
					// node has no right child
					if (node.right == null) {
						return node.left;
					}
					// node has two children
					let tempNode = node.right;
					while (tempNode.left !== null) {
						tempNode = tempNode.left;
					}
					node.data = tempNode.data;
					node.right = removeNode(node.right, tempNode.data);
					return node;
				} else if (data < node.data) {
					node.left = removeNode(node.left, data);
					return node;
				} else {
					node.right = removeNode(node.right, data);
					return node;
				}

				this.root = removeNode(this.root, data);
			}
		}
	}

	var bst = new BST();
	bst.add(7);
	bst.add(2);
	bst.add(6);
	bst.add(1);
	bst.add(3);
	bst.add(5);
	bst.add(4);
	bst.remove(7);
	console.log(bst.findMin());
	console.log(" max value is " + bst.findMax());
	bst.remove(7);
	console.log(" max value is: " + bst.findMax())
	console.log(bst.isPresent(4));