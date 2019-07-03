def func(list_in):
	out = []
	for i in list_in:
		if i > -1:
			yield i

a = [-1, -2, 1, 2]
print(list(func(a)))

