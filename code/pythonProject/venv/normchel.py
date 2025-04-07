'''b = list()


def matrica(n=1, m=None, a=0):
	if m is None and n:
		m = n
	for i in range(n):
		b.append(a)
	for i in range(m):
		print(*b)


matrica(int(input()), int(input()), int(input()))'''
def matrix(n=1, m=None, a=0):
	if m is None and n:
		m = n
	return[[a] + i for range(m)] + i for range(n)


rows = matrix(2)
for row in rows:
	print(*row)
