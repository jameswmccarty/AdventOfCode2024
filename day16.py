#!/usr/bin/python

# Advent of Code 2024 Day 16

import heapq

def bfs(start, end, walls):
	seen = set()
	q = []
	heapq.heapify(q)
	dirs = [(1,0),(0,-1),(-1,0),(0,1)]
	seen.add((start,0))
	heapq.heappush(q, (0,start,0))
	while q:
		score, pos, facing = heapq.heappop(q)
		if pos == end: return score
		x, y = pos
		dx, dy = dirs[facing]
		nx, ny = x+dx, y+dy
		if (nx, ny) not in walls and ((nx, ny), facing) not in seen:
			seen.add(((nx,ny),facing))
			heapq.heappush(q,(score+1,(nx,ny),facing))
		if (pos, (facing+1)%4) not in seen:
			seen.add((pos, (facing+1)%4))
			heapq.heappush(q,(score+1000,pos,(facing+1)%4))
		if (pos, (facing-1)%4) not in seen:
			seen.add((pos, (facing-1)%4))
			heapq.heappush(q,(score+1000,pos,(facing-1)%4))
	return "None"

if __name__ == "__main__":

	# Part 1 Solution
	walls = set()
	start = None
	end = None
	with open("day16_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == '#': walls.add((x,y))
				elif char == 'S': start = (x,y)
				elif char == 'E': end = (x,y)
			y = y + 1
	print(bfs(start, end, walls))


	# Part 2 Solution

