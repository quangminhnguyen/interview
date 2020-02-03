

# Find K largest element in an array 
# Solution: keep a queue of k biggest elements so far sorted in descending order while iterating through the items in the array.


# Find the k-largest elements in the array 
# Parameters:
# 		array - array of items to search for k-leargest lements 
#		k - number of largest elements to find
def find_k_largest( array, k ):
	queue = [];
	queue_length = 0;

	for i in range( len( array ) ):
		cur_val = array[i];

		if ( queue_length == 0 ):
			queue.insert( 0, cur_val );
			queue_length = queue_length + 1;
		else:
			j = 0;
			while ( j < queue_length ):
				if ( array[j] >= cur_val ): # sorted in descending order makes item removal more efficient
					j = j + 1;
				else:
					break;

			queue.insert( j, cur_val );
			queue_length = queue_length + 1;

			if ( queue_length > k ):
				queue.pop(); # the last items in the list

	return queue;


if __name__ == "__main__":
	a = [ 38, 24, 31, 14, 11, 22, 33, 51, 32, 22, 21, 21, 42 ];
	k_largest = find_k_largest( a, 2 );
	print( "k_largest", k_largest );