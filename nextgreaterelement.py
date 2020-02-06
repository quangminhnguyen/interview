
'''
	Return the next greater elements for every value in the array
	e.g. [2, 3, 5, 7] ==> [2, 3, 5, -1]. No element on the right of
	7 is bigger than it.
	O(n^2) solutions
'''
def next_greater_elems( array ):
	greater_elems = [];
	for i in range( len( array ) ):
		flag = False;
		for k in range( i + 1, len( array ), 1 ):
			if ( array[i] < array[k] ):
				greater_elems.append( array[ k ] );
				flag = True;
				break;

		# No element on the right of array[i] is greater than it
		if (flag == False):
			greater_elems.append( -1 );
			
	print( "greater elements", greater_elems );



def next_greater_elems2( array ):
	temp = []; # acts as a stack.
	rs = [-1] * len(array);
	for i in range( len( array ) ):
		if ( len( temp ) == 0 ):
			temp.append( i );
		elif ( len( temp ) > 0 ):
			k = len(temp) - 1;
			while ( k >= 0 ):
				if ( array[temp[k]] <= array[i] ):
					rs[temp[ k ]] = array[ i ];
				k = k - 1;
			temp.append( i );
	return rs;



if __name__ == '__main__':
	asd_array = [1, 2, 3, 4, 5];
	dsd_array = [5, 4, 3, 2, 1];

	rs1 = next_greater_elems( asd_array );
	rs2 = next_greater_elems( dsd_array );

	print( "rs1", rs1 ); # expect to be [2, 3, 4, 5, -1]
	print( "rs2", rs2 ); # expect all to be -1


	print( "Test" );
	rs3 = next_greater_elems2( asd_array );
	print( "rs3", rs3 )
























# compare with the elem in the stack
# while ( True ): 
#	if (arr[temp[len[temp] - 1]] <= arr[i]):
#		rs[temp[ len[temp] - 1]] = arr[i];
#		temp.append(i);
#		temp.pop();
#	else:
#		temp.append(i);


# temp.append( i ); 

'''
	Leverages the last in first out of Stack datastructure to develop an O(n) solution
'''
# class Node:
#     def __init__( self, value ):
#     	self.value = value; # 
#     	self.next = None; # pointer to the next element in the stack
#     	self.last = None; 

# class Stack:
# 	def __init__( self ):
# 		self.start = None;
# 		self.end = None;
# 		self.length = 0;

# 	def push( self, new_node ):
# 		if ( self.start == None ):
# 			self.start = new_node;
# 			self.end = new_node;
# 			self.length = self.length + 1;

# 		elif ( self.start != None ):
# 			self.end.next = new_node;
# 			new_node.back = self.end;
# 			self.end = new_node;
# 			self.length = self.length + 1; 


# 	def pop( self ):
# 		if ( self.start == None ):	
# 			return;
		
# 		if ( self.start == self.end ):
# 			copyend = self.start;
# 			self.start = None;
# 			self.end = None;
# 			self.length = 0;
# 			return copyend;

# 		copyend = self.end;
# 		self.end.back.next = None;
# 		self.end = self.end.back
# 		self.length = self.length - 1;
# 		return copyend;

# 	def get_last_element( self ):
# 		return self.end;

# 	def length( self ):
# 		return self.length;


# def next_greater_elems2( array ):
# 	stack = Stack();
# 	rs = [];
# 	for i in range( len( array ) ):
# 		if ( stack.length == 0 ):
# 			stack.push( Node( array[i] ) );
# 		elif ( stack.length > 0 ):
# 			stack_val = stack.get_last_element().value;
# 			while( stack_val <= array[i] and stack.length > 0 ):
# 				rs.append( array[i] );			
# 				#stack_val = stack.get_last_element().value;
# 				stack.pop();
# 				stack_val = stack.get_last_element().value;
			
# 			stack.push( Node( array[i] ) );

# 	while (stack.length > 0):
# 		rs.append( -1 );
# 		stack.pop();

# 	return rs;
			# stack.push( Node( array[ i ] ) );