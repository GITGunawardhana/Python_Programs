def sort_list(list1, list2):
	zippedPairs = zip(list2, list1)
	listZ = [x for i, x in sorted(zippedPairs)]
	return listZ
	
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]
print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
print(sort_list(x, y))
