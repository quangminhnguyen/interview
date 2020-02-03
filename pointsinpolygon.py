
import math;

# Determine the set of points in a polygon
# Solution: Ray-length algorithms 
# 2 keys:
# [1] Draw a horizontal line to the right of every point and count the number of intersections
#     if touch one time but lying directly on top of a corner of a polygon <=> inside the polygon
#     odd number of intersection <=> inside the polygon
#     even number of intersection <=>  outside the polygon 		    
# [2] Solve linear equation to find the intersection between 2 line segments 

'''
	Calculates the direct distance between two points (i.e., point1 and point2)
	Parameters: 
		point1 - coordinate of point2
		point2 - coordinate of point1
	Return: 
		boolean - determine whether the point is in the polygon
'''
def distance_between_two_points( point1, point2 ):
	distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** (0.5);
	return distance;


'''
	Checks if a point is in the polygon
	Parameters:	
		point - coordinate of the point to be checked
		polygon - list of coordinate tuples that define the polygon 
	Return: 
		boolean - determine whether point is in the polygon
'''
def is_point_in_polygon( point, polygon ):

	# special case where the point lie directly on top of the polygon
	if (point in polygon):
		return True;

	max_x =  max( [x for (x, y) in polygon] ) ;
	end_x = max_x + 1;
	end_y = point[1];

	segment1 = ( point, (end_x, end_y) );

	intersect_count = 0;
	for i in range(len(polygon) - 1): 
		segment2 = ( polygon[i], polygon[i + 1] );
		if ( is_intersect( segment1, segment2 ) ):
			intersect_count = intersect_count + 1;
		# or online 
	
	if ( intersect_count % 2 == 1):
		return True;
	return False;


'''
	Determines the gradient and y intercept of a line
	Parameters:
		point1 - coordinate of the start point of the line segment 
		point2 - coordinate of the end point of the line segment
'''
def get_gradient_and_y_intercept( point1, point2 ):
	gradient = (point2[1] - point1[1]) / float( point2[0] - point1[0]) ;
	y_intercept = point1[1] - gradient * float(point1[0]);
	return ( gradient, y_intercept );


'''
	Checks whether the two lines are intersect
	Parameters:	
		segment1 - line segment1 spciefied by the start and end coordinates
		segment2 - line segment1 spciefied by the start and end coordinates
	Return: 
		boolean - determine whether point is in the polygon
'''
def is_intersect( segment1, segment2 ):
	point1_segment1 = segment1[0];
	point2_segment1 = segment1[1];
	point1_segment2 = segment2[0];
	point2_segment2 = segment2[1];

	gradient1, y_intercept1 = get_gradient_and_y_intercept( point1_segment1, point2_segment1 );
	gradient2, y_intercept2 = get_gradient_and_y_intercept( point1_segment2, point2_segment2 );


	# Presumbly intersect point
	y = (gradient2 * y_intercept1 - gradient1 * y_intercept2) / (gradient2 - gradient1);
	if (gradient1 != 0):
		x = (y - y_intercept1) / gradient1; 
	else: 
		x = (y - y_intercept2) / gradient2;	


	# Is the intersect point lies on the segment
	minxs1 = min( point1_segment1[0], point2_segment1[0] );
	maxxs1 = max( point1_segment1[0], point2_segment1[0] );
	minys1 = min( point1_segment1[1], point2_segment1[1] );
	maxys1 = max( point1_segment1[1], point2_segment1[1] );
	on_segment1 = ( minxs1 <= x <= maxxs1) and ( minys1 <= y <= maxys1 ) ;  
	
	minxs2 = min( point1_segment2[0], point2_segment2[0] );
	maxxs2 = max( point1_segment2[0], point2_segment2[0] );
	minys2 = min( point1_segment2[1], point2_segment2[1] );
	maxys2 = max( point1_segment2[1], point2_segment2[1] );
	on_segment2 = (minxs2 <= x <= maxxs2) and ( minys2 <= y <= maxys2 );


	return on_segment1 and on_segment2;

if __name__ == "__main__":

	polygon = [ (1, 1), (0, 3), (3, 4), (5, 1) ];
	points = [ ( 1, 1 ), ( 2, 2 ), ( 3, 3 ), ( 0, 0 ), ( 5, 5) ]; # expect: true, true, true, false, false
	results = [];


	for point in points:
		results.append( is_point_in_polygon( point, polygon ) );

	print( "results", results ); 


