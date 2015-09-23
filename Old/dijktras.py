#!/usr/bin/env python3

#	Author: Christopher Lillthors
#	Licence: MIT

import heapq as hq
import sys
import math
inf = math.inf

# Return the minimal distance between source and target in graph G.
def hard_way(G,dikes,source,target):
	if source == target:
		return 0 # We haven't moved so the distance must be 0

	q = [] # Heap queue
	dist = [None] * len(G)	# Preallocate memory.

	# Make sure to mark where we came from.
	dist[source] = 0
	for v in range(len(G)):
		if v != source:
			dist[v] = inf
		hq.heappush(q,v)

	while len(q) != 0:
		u = hq.heappop(q) # Remove and return the smallest item.
		if u == target:
			break # We found our target ^^

		for v in range(len(G[u])):
			alt = dist[u] + G[u][v]
			if (v,u) in dikes:
				alt += 100 # Add 100 in cost for dike.
			if alt < dist[v]:
				dist[v] = alt #	Update! We found a new better route.
	return dist[target]

def main(source, target):
	G = [
    	[0, 2, inf, 3],
    	[inf, 0, 4, inf],
    	[inf, inf, 0, 5],
    	[inf, inf, inf, 0]
    ]
	dikes = [(0,2),(1,2)]

	n = len(G)
	if source < n and target < n:
		print('Running dijktras...')
		dist = hard_way(G,dikes,source,target) # Get an array of distances.
		if dist != inf:
			print(('Distances from {:d} -> {:d} ==> ').format(source,target),dist)
		else:
			print(('Could not find a path between {:d} and {:d}').format(source,target))
	else:
		error = ('Cannot find vertices {:d} and {:d}').format(source,target)
		sys.exit(error)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(('Usage: {:s} from target').format(sys.argv[0]))
	else:
		[_,source,target] = sys.argv
		try:
			sourceNumber = int(source)
			targetNumber = int(target)
			main(sourceNumber,targetNumber)
		except ValueError:
			error = "Input error: Tried to convert {:s} and {:s} into numbers".format(source,target)
			sys.exit(error)
