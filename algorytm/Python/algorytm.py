def algorytm(array):
	# Keep track of smallest in
	smallest = 1


	# Sort the array
	array.sort()

	if array[-1] <= 0:
		return smallest


	for i in array:
		if i > smallest:
			return smallest
		elif i == smallest:
			smallest+=1

	return smallest


test1 = [3, 5, -2, 2, 1, 8, 15] #4
test2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #2
test3 = [-5, -3, 0, 0, -2] #1

print(algorytm(test1))
print(algorytm(test2))
print(algorytm(test3))