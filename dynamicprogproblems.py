

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
	Parameter:
		string - input string 
	Return:
		longest palimodrome
'''
def longest_palimodrome_subsequence( string ):
	if len(string) == 0:
		return 0;

	if len(string) == 1:
		return 1;
	
	if string[0] == string[-1]:
		return longest_palimodrome_subsequence( string[1: -1] ) + 2; 

	elif string[0] != string[-1]:
		return max( longest_palimodrome_subsequence( string[: -1] ), longest_palimodrome_subsequence( string[1:] )); 
	
		
'''
	Dynamic solution
	Parameter: 
		string -  input string
	Return:
		longest palimodrome
'''
def longest_palimodrome_subsequence2( string ):

	temp = [[0 for i in range(len(string)) ] for j in range(len(string)) ];

	for ssl in range( len(string) ):
		for start in range( len(string) ):
			end = min( len(string) - 1, start + ssl);
			temp[start][end];
			if (start == end):
				temp[start][end] == 1
			elif (start != end):
				if string[start] == string[end]:
					if end == (start + 1):
						temp[start][end] = 2;
					else:
						temp[start][end] = temp[start + 1][end - 1] + 2;
				elif string[start] != string[end]:	
					if end == (start + 1):
						temp[start][end] = 0;
					else:
						temp[start][end] = max( temp[start + 1][end], temp[start][end - 1] );
	return temp[0][len(string) - 1];



			



if __name__ == '__main__':
	string = 'abccba';
	print( "test ", is_palimodrome( string ));
	print( "longest palimodrome without memorization", longest_palimodrome_subsequence( string ) ); 
	print( "longest palimodrome with memorization", longest_palimodrome_subsequence2( string ) ); 
















	# def longest_palimodrome_subsequence2( string ):
# 	temp = [[0 for i in range(len(string) + 1) ] for j in range(len(string) + 1) ];

# 	# ssl = substring length
# 	for ssl in range( 1, len( string ) + 1 ):
# 		for start in range( len(string) ):
# 			#print( "-------" );
# 			end = min( len(string) , start + ssl );
# 			#print( "start", start );
# 			#print( "end", end );
# 			#print( "ssl", ssl );
# 			if (start == end): 
# 				temp[start][end] = 0;
# 			elif (end == start + 1):
# 				temp[start][end] = 1;
# 			else:
# 				if (string[start] == string[end - 1]):
# 					temp[start][end] = temp[start + 1][end - 2] + 2;
# 				elif (string[start] != string[end - 1]):
# 					temp[start][end] = max(temp[start + 1][end - 1], temp[start][end - 2]);
# 	return temp;