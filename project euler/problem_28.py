class NumberCircle(object):
    """
    NumberCircle to find the triangle number. for example:
    7 8 9
    6 1 2
    5 4 3
    The triangle value for circle 2 is 7,9,5,3
    """
    
    def __init__(self, edge):
        """
        init with the edge length 
        """
        self.edge = edge

    def sum(self):
        edge_upper_right = self.edge**2
        edge_upper_left = edge_upper_right-self.edge+1
        edge_down_left = edge_upper_left-self.edge+1
        edge_down_right = edge_down_left-self.edge+1
        return edge_upper_left + edge_upper_right + edge_down_left +edge_down_right

result = 1
for index in xrange(3, 1003,2):
    result += NumberCircle(index).sum()
print result


result = 1
for index in xrange(3, 7,2):
    result += NumberCircle(index).sum()
print result
        
        
        