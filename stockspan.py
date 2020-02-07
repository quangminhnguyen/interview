# Stock span problem = this is like a backward next greater problem
# https://www.geeksforgeeks.org/the-stock-span-problem/


'''
	Example: [ 100, 80, 60, 70, 60, 75, 85 ]
	Return: [1, 1, 1, 2, 1, 4, 6]
	O(n^2) implementation
'''
def calculate_stockspan( arr ):
	i = len( arr ) - 1;
	rs = [0] * len(arr);
	while ( i >= 0 ):
		k = i;
		count = 0;
		while ( k >= 0 and arr[k] <= arr[i] ):
			count = count + 1;
			k = k - 1;
		rs[i] = count;
		i = i - 1;
	return rs;


'''
	Example: [ 100, 80, 60, 70, 60, 75, 85 ]
	Return: [1, 1, 1, 2, 1, 4, 6]
	Is it O(n) ?
'''
def calculate_stockspan2( arr ):
	i = len( arr ) - 1
	rs = [1] * len(arr);
	stack = []; # acts like a stack
	while ( i >= 0 ):
		if ( len(stack) == 0 ):
			stack.append( i );
		else: # len( stack ) > 0
			k = len(stack) - 1 ; # top of the stack
			while ( k >= 0 ):
				if  arr[i] > arr[stack[k]]:
					rs[stack[k]] = stack[k] - i;
					stack.pop( k );
				k = k - 1;
			stack.append( i );
		i = i - 1;		

	return rs;



if __name__ == "__main__":
	arr = [ 100, 80, 60, 70, 60, 75, 85 ];
	print( "stock span", calculate_stockspan( arr ) );

	print( "stock span2", calculate_stockspan2( arr ) );