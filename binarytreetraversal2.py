class Node:

    def __init__(self, value):

        self.left = None; # turn into back pointer in doubly linked list
        self.right = None # turn into next pointer in doubly linked list
        self.value = value


    # Left order tree traversal: left - root -right
    def print_tree( self ):
    	if self.left:
    		self.left.print_tree();
    	print( self.value );
    	if self.right:
    		self.right.print_tree();

    # Prints doubly linked list
    def print_LL( self ):
    	curr = self;
    	while ( curr ):
    		print( curr.value );
    		curr = curr.right;

'''
	Covert a binary tree into a doubly linked list
	Parameters: 
		root - root node of the tree
		LLhead - head of the linked list
	Return 
		LLhead - head of the linked list.
'''
def TreetoDLL( root, LLhead ):

	if ( root == None ):
		return None;

	# Recursively construct DLL for right subtree if it actually exist
	if ( root.right ):
		LLhead = TreetoDLL( root.right, LLhead );

	root.right = LLhead; # pointing to the head of the DLL created for the right subtree
	if ( LLhead ):
		LLhead.left = root; # having the back pointer pointing to the root 
	LLhead = root; # make the root the start of the linked list

	if ( root.left ):
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

	DLL = TreetoDLL( root, None );
	DLL.print_LL();
















# def TreetoDLL2( root, LLhead ):
# 	print( "-----" );
# 	if ( root ):
# 		print( "root", root.value );
# 	else:
# 		print( "root None" );

# 	if ( root.right ):
# 		LLhead = TreetoDLL2( root.right, LLhead );

# 	root.right = LLhead;

# 	if ( LLhead ):
# 		LLhead.left = root;

# 	LLhead = root;

# 	print( "middle LLhead", LLhead.value );

# 	if ( root.left ):
# 		LLhead = TreetoDLL2( root.left, LLhead );

# 	if ( LLhead ):
# 		print( "LLhead", LLhead.value );
# 	else:
# 		print( "LLhead Null ");

# 	return LLhead;



# def TreetoDLL( root, LLhead ):

# 	if ( root ):
# 		print( "root", root.value );
# 	else:
# 		print( "root None" );


# 	if ( root == None ):
# 		return None;

# 	# Recursively convert the right subtree
# 	LLhead = TreetoDLL( root.right, LLhead );

# 	root.right = LLhead;

# 	if ( LLhead ):
# 		LLhead.left = root;

# 	LLhead = root;

# 	LLhead = TreetoDLL( root.left, LLhead );

# 	if ( LLhead ):
# 		print( "LLhead", LLhead.value );
# 	else:
# 		print( "LLhead Null ");

# 	return LLhead;