# Question: 
# Implement a datastructure that provide push/pop/min/length operations in O(1)

# Unlike queue which are first-in, first-out, in stacks, the elements that lasted pushed to the stack is also the first one that gets poped out of the stack
class Node:
    def __init__( self, value ):
    	self.value = value; # 
    	self.next = None; # pointer to the next element in the stack
    	self.last = None; 

class Stack:
	def __init__( self ):
		self.start = None;
		self.end = None;
		self.length = 0;

	def push( self, new_node ):
		if ( self.start == None ):
			self.start = new_node;
			self.end = new_node;
			self.length = self.length + 1;

		elif ( self.start != None ):
			self.end.next = new_node;
			new_node.back = self.end;
			self.end = new_node;
			self.length = self.length + 1; 


	def pop( self ):
		if ( self.start == None ):	
			return;
		
		if ( self.start == self.end ):
			copyend = self.start;
			self.start = None;
			self.end = None;
			self.length = 0;
			return copyend;

		copyend = self.end;
		self.end.back.next = None;
		self.end = self.end.back
		self.length = self.length - 1;
		return copyend;



	def length( self ):
		return self.length;

if __name__ == '__main__':
	n1 = Node( '1' );
	n2 = Node( '2' );
	n3 = Node( '3' );

	stack = Stack();
	stack.push( n1 );
	stack.push( n2 );
	stack.push( n3 );


	print( stack.pop().value );
	print( stack.pop().value );
	print( stack.pop().value );

	#print( stack.pop().value );
	#print( stack.pop().value );

	#print( "stack.value ",  stack..pop );
	#print( "stack.next.value", stack.next.value );
	#print( "stack.next.next.next.value", stack.next.next.value );

