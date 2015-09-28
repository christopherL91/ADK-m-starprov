#!/usr/bin/env python3
import heapq as hq
import math
import sys
inf = math.inf

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def setup(data,dykes):
    grid = {}
    for i,rows in enumerate(data):
        for j,val in enumerate(rows):
            vertice = {'up':inf,'down':inf,'left':inf,'right':inf}

            current_pos = (i,j)
            up_pos = (i-1,j)
            left_pos = (i,j-1)
            right_pos = (i,j+1)
            down_pos = (i+1,j)
            extra_costs = [0] * 4
            if current_pos in dykes:
                #   We have atleast one dyke.
                for pos in dykes[current_pos]:
                    if pos == up_pos:
                        extra_costs[0] = 100
                    elif pos == down_pos:
                        extra_costs[1] = 100
                    elif pos == left_pos:
                        extra_costs[2] = 100
                    elif pos == right_pos:
                        extra_costs[3] = 100

            if i != 0:
                vertice['up'] = data[i-1][j] + extra_costs[0]
            if i != len(data) - 1:
                vertice['down'] = data[i+1][j] + extra_costs[1]
            if j != 0:
                vertice['left'] = data[i][j-1] + extra_costs[2]
            if j != len(rows) - 1:
                vertice['right'] = data[i][j+1] + extra_costs[3]
            grid[current_pos] = vertice
            # print(current_pos,grid[current_pos])
    return grid

def astar(gamegrid,size):
    start_pos = (0,0)
    end_pos = (size-1,size-1)
    visited = {}
    total = 0
    costs = {start_pos:0}
    q = []

    hq.heappush(q,(0,start_pos))
    while len(q) != 0:
        current = (i,j) = hq.heappop(q)[1]
        visited[current] = True

        if current == end_pos:
            break

        cost_list = gamegrid[current]
        min_op = min(cost_list,key=cost_list.get)
        cost_next_move = cost_list[min_op]
        print(min_op)

        next_pos = []
        if min_op == 'up':
            next_pos = (i-1,j)
            gamegrid[next_pos]['down'] = inf
        elif min_op == 'left':
            next_pos = (i,j-1)
            gamegrid[next_pos]['right'] = inf
        elif min_op == 'right':
            next_pos = (i,j+1)
            gamegrid[next_pos]['left'] = inf
        elif min_op == 'down':
            next_pos = (i+1,j)
            gamegrid[next_pos]['up'] = inf

        new_cost = costs[current] + cost_next_move

        if new_cost > 50:
            print('not able to jump anymore')

        if  next_pos not in visited and new_cost < costs.get(next_pos,inf):
            costs[next_pos] = new_cost
            priority = new_cost + heuristic(end_pos,next_pos)
            hq.heappush(q,(priority,next_pos))
            visited[next_pos] = True
    return costs.get(end_pos,None)

if __name__ == "__main__":
    data =  [
            [0,20,50,10,20,10],
            [5,6,10,100,50,10],
            [40,3,2,1,6,30],
            [10,60,70,30,20,10],
            [40,10,20,80,30,10],
            [10,10,10,10,10,10]
        ]
    dykes = {
        (0,0):[(1,0)],
        (3,2):[(3,3)]
    }

    gamegrid = setup(data,dykes)
    cost = astar(gamegrid,len(data))
    if cost == None:
        sys.exit("Impossibruuuuu!!!")
    print(cost)
