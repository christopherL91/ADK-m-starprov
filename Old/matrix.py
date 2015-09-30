#!/usr/bin/env python3

from itertools import tee, chain

def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)

if __name__ == '__main__':
	matrix = [
		[2,3,1,4],
		[3,3,3,3],
		[5,3,2,2],
		[2,1,2,4]
	]
	num = 0
	for row in range(1,len(matrix)): #	O(n)
		for (v, w) in pairwise(zip(matrix[row-1],matrix[row])):
			square = list(chain.from_iterable([v,w]))
			mean = sum(square)//len(square)
			num += len(list(filter(lambda x: x > mean, square)))
	print('answer',num)
