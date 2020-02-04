

# tree traversal with recursion


'''
	Tree inorder traversal - left - root - right
	Parameters:
		tree - A complete binary search tree represented by an array
		i - index of root node
	Return:
		in order traversal of the tree 
'''
def in_order( tree, i ):
	result = [];
	if ( 2 * i + 1 < len( tree ) ):
		result = result + in_order( tree, 2 * i + 1 );
	result = result + [tree[i]];
	if ( 2 * i + 2 < len( tree ) ):
		result = result + in_order( tree, 2 * i + 2 );
	return result;
	

'''
	Tree preorder traversal - root - left - right
	Parameters:
		tree - A complete binary search tree represented by an array
		i - index of root node
	Return:
		pre order traversal of the tree 
'''
def pre_order( tree, i ):
	result = [tree[i]];
	if ( 2 * i + 1 < len( tree ) ):
		result = result + in_order( tree, 2 * i + 1 );
	if ( 2 * i + 2 < len( tree ) ):
		result = result + in_order( tree, 2 * i + 2 );
	return result;

'''
	Calculates depth of a tree
	Parameters:
		tree - A complete binary search tree represented by an array
		i - index of root node
	Return:
		depth of the given tree
'''
def calculate_depth( tree, i ):
	if ( ( 2 * i + 1 ) >= len( tree ) and ( 2 * i + 2 ) >= len( tree ) ):
		return 0;
	elif ( ( 2 * i + 1 ) >= len(tree) ):
		return calculate_depth( tree, 2 * i + 2 ) + 1;
	elif ( ( 2 * i + 2 ) >= len(tree) ):
		return calculate_depth( tree, 2 * i + 1 ) + 1;
	else:
		return max( calculate_depth( tree, 2 * i + 1 ) + 1, calculate_depth( tree, 2 * i + 2 ) + 1 );
		


'''
	Calculates number of leaves in the tree 
	Parameters:
		tree - A binary tree
		i - index of the current root node 
	Return:
		number of leaves in the tree
'''
def count_leave( tree, i ):
	if ( ( 2 * i + 1 ) >= len( tree ) and ( 2 * i + 2 ) >= len( tree ) ):
		return 1;
	elif ( ( 2 * i + 1 ) >= len(tree) ):
		return count_leave( tree, 2 * i + 2 );
	elif ( ( 2 * i + 2 ) >= len(tree) ):
		return count_leave( tree, 2 * i + 1 );
	else:
		return count_leave( tree, 2 * i + 2 ) + count_leave( tree, 2 * i + 1 );


if __name__ == "__main__":

	# A binary search tree
	bst = [ 25, 18, 28, 10, 23, 26, 30, 8, 15, 20, 24 ];
	
	print( "In-order tree traversal", in_order( bst, 0 ) );	
	print( "Pre-order tree traversal", pre_order( bst, 0 ) );
	print( "Tree-depth", calculate_depth( bst, 0 ) );
	print( "Count number of leaves", count_leave( bst, 0 ) );

	# post-order: left right root 
	# pre-order: root left right 
	# inorder: left right root