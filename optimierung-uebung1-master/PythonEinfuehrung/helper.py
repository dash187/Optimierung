def my_square_function(x):
	""" :returns the squared input and the gradient"""
	square = [elt**2 for elt in x]
	grad = [2*elt for elt in x]
	return square, grad