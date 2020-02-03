

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



if __name__ == "__main__":

	# A binary search tree
	bst = [ 25, 18, 28, 10, 23, 26, 30, 8, 15, 20, 24 ];
	
	print( "In-order tree traversal", in_order( bst, 0 ) );	
	print( "Pre-order tree traversal", pre_order( bst, 0 ) );