#!/usr/bin/env python3
import heapq as hq
import itertools

#	Indata [t1,t2,t3,...,tn]

def solve(queue):
	COST = 100
	result = 0
	while len(queue) != 0:
		time = hq.heappop(queue)
		result += time * COST + len(queue) * COST * time
	return result

def solve_greedy(times):
	COST = 100
	result = 0
	while len(times) != 0:
		time = times.pop(0)
		result += time * COST + len(times) * COST * time
	return result
if __name__ == '__main__':
	times = [2,3,5]
	results = []
	# hq.heapify(times)
	for perm in itertools.permutations(times):
		result = solve_greedy(list(perm))
		results.append((perm,result))
		# print(('{} ==> {:d}').format(perm,result))
	results.sort()
	q = []
	for res in results:
		hq.heappush(q,res[1])
		print(('{} ==> {:d}').format(res[0],res[1]))

	print('Minimal cost', hq.heappop(q))
