#!/usr/bin/python

# Advent of Code 2024 Day 21

import heapq

alpha_pad = ['789','456','123',' 0A']
dir_pad = [' ^A','<v>']
delta = {(0,1):'v',(0,-1):'^',(1,0):'>',(-1,0):'<'}

alpha_routes = dict()
dir_routes = dict()

def routes(start_char, end_char, pad):
	for y in range(len(pad)):
		for x in range(len(pad[0])):
			if pad[y][x] == start_char:
				start = (x,y)
			if pad[y][x] == end_char:
				end = (x,y)
	routes = set()
	shortest = float('inf')
	q = [(0,start,{},'')]
	while q:
		steps, loc, seen, path = q.pop(0)
		if loc == end:
			if steps <= shortest:
				shortest = steps
				routes.add(path+'A')
		x, y = loc
		for dx,dy in delta.keys():
			nx, ny = x+dx, y+dy
			if nx >= 0 and nx < len(pad[0]) and ny >= 0 and ny < len(pad):
				if pad[ny][nx] not in seen and pad[ny][nx] != ' ':
					q.append((steps+1,(nx,ny),{*seen,pad[ny][nx]},path+delta[(dx,dy)]))
	return routes

for a in '0123456789A':
	for b in '0123456789A':
		alpha_routes[a+b] = routes(a,b,alpha_pad)

for a in '<v>^A':
	for b in '<v>^A':
		dir_routes[a+b] = routes(a,b,dir_pad)

def next_level(line):
	routes = {''}
	while len(line) > 1:
		routes = { r+e for e in dir_routes[line[0]+line[1]] for r in routes}
		line = line[1:]
	return routes

if __name__ == "__main__":

	score = 0
	# Part 1 Solution
	with open("day21_input", "r") as infile:
		for line in infile:
			start = 'A'+line.strip()
			routes = {''}
			while len(start) > 1:
				routes = { r+e for e in alpha_routes[start[0]+start[1]] for r in routes }
				start = start[1:]
			q = []
			heapq.heapify(q)
			for entry in routes:
				heapq.heappush(q,(len(entry),1,entry))
			while True:
				factor, depth, route = heapq.heappop(q)
				if depth == 3:
					print(factor, route)
					break
				for entry in next_level('A'+route):
					heapq.heappush(q,(len(entry),depth+1,entry))
			score += int(''.join(x for x in line if x in '0123456789')) * factor
	print(score)
	# Part 2 Solution

