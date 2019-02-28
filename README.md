# GINI_Index_python
GINI Index Calculator in Pyhton, using numpy package

The package can be imported as: 'import gini_package.gini'
the functions available now:

	gini(characteristic, class)

		characteristic: array of size n, containing binary values of the characteristic (e.g: [1,0,0,1,0,1])

		class: array of size n, containing binary values of the class (e.g: [0,1,0,1,0,0])

		returns:

			int value, gini index of the characteristic with the class
			
			
Example of use:

	import gini_package.gini as gp
	toto = [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
	foo = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
	gp.gini(toto, foo)
	
	
	>>0.047815820543093246
	

Future Changes Planned:
	
	*Add an easier way to give the input, such as taking a 2d array and getting the values directly from it, and the last 1d array of the 2d array is the class
	*Add a possible formatting to the output (e.g: Student factor: 0.142098...)
