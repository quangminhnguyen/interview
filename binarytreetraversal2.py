class Node:

    def __init__(self, value):

        self.left = None; # turn into back pointer in doubly linked list
        self.right = None # turn into next pointer in doubly linked list
        self.value = value


    # left order tree traversal: left - root -right
    def print_tree( self ):
    	if self.left:
    		self.left.print_tree();
    	print( self.value );
    	if self.right:
    		self.right.print_tree();

# class DoublyLL:

# 	def __init__(self, value):
# 		self.back = None;
# 		self.forward = None;
# 		self.value = value;

'''
	Convert a binary tree into a doubly linked list using reverse inorder traversal.
'''
def TreetoDLL( root, LLhead ):

	if ( root == None ):
		return None;

	# Recursively convert the right subtree
	LLhead = TreetoDLL( root.right, LLhead );

	root.right = LLhead;

	if ( LLhead ):
		LLhead.left = root;

	LLhead = root;

	LLhead = TreetoDLL( root.left, LLhead );

	return LLhead;


def TreetoDLL2( root, LLhead ):
	

	if ( root.right ):
		LLhead = TreetoDLL( root.right, LLhead );

	root.right = LLhead;

	if ( LLhead ):
		LLhead.left = root;

	LLhead = root;

	if ( root.left, LLhead ):
		LLhead = TreetoDLL( root.left, LLhead );

	return LLhead;


if __name__ == "__main__":

	root = Node( 10 );
	root.left = Node( 5 );
	root.right = Node( 15 );
	root.left.left = Node( 2 );
	root.left.right = Node( 7 );
	root.right.left = Node( 12 );
	root.right.right = Node( 18 );

	DLL = TreetoDLL(root, None);
	DLL.print_tree;

	
	# LL = TreetoDLL( root, None ); 

	# LL.print_tree();
	# root.print_tree();
	# root.print_node();