def func(list_in):
	for i in list_in:
		if i >= 0:
			yield i

a = [-1, -2, 1, 2]
print(list(func(a)))
b = lambda x: [i for i in x if i >=0]
print(b(a))
