
'''
	Returns the longest common prefix for the strings in array O(n^2)
	Parameters:
		array - list of strings
	Return:
		longest common prefix
'''
def longest_common_prefix( array ):
	longest = '';
	for i in range( len(array) ):
		str1 = array[i];
		for j in range( len(array) ):
			str2 = array[j];
			min_length = min( len(str1), len(str2) );
			for k in range( min_length ):
				if ( str1[:k] == str2[:k] ): 
					if ( k > len( longest ) ):
						longest = str1[:k];
	return longest;

if __name__ == "__main__":

	array = ["test1", "test2", "test3", "test14", "test5"];
	print( longest_common_prefix( array ) ); # expected solution: test11


