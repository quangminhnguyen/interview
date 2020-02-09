

# Detect whether a word is a palindrome
# aba is a palimodrome
'''
	Input:
		string - input string
	Return: 
		Whether str is a palindrome string 
'''
def is_palimodrome( string ):
	if len( string ) == 1:
		return True;
	elif len( string ) == 2:
		return True;
	else:
		return [string[i] for i in range(len(string))] == [string[i] for i in range(len(string) -1, -1, -1)];

'''
	Recursive solution without memorizing
'''
def longest_palimodrome_subsequence( string ):
	if len(string) == 0:
		return True;

	if len(string) == 1:
		return True;
	
	if string[0] == string[-1]:
		return longest_palimodrome_subsequence( string[1: -1] ) + 2; 

	elif string[0] != string[-1]:
		return max( longest_palimodrome_subsequence( string[: -1] ), longest_palimodrome_subsequence( string[1:] )); 
	
		
'''
	Recursive solution with memorization
'''
def longest_palimodrome_subsequence( string ):
	#
	# 0 - default value, -1 - is a palimdrome, 1 - is not a pali
	temp = [[0 * len(string)] * len(string)];
	for i in range( len( string ) ):
		for j in range( i, len( string ), 1 ): 
			if ( (i == j) or (j == i + 1) ):
				temp[i][j] = 1;
				continue;
			else:
				temp[i][j] = 0;

				# temp[i][j] 

				# temp[i][j] = 1;



			#if temp[i][j] == 0:
			#	temp[i][j] = longest_palimodrome_subsequence


				# temp[][]

			# if ( i == j or j = i + 1 or i = j + 1 ):
			



if __name__ == '__main__':
	string = 'abccba';
	print( "test ", is_palimodrome( string ));
	print( "longest palimodrome", longest_palimodrome_subsequence( 'abcdef' ) ); 