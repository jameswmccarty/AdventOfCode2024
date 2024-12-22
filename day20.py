#!/usr/bin/python

# Advent of Code 2024 Day 20

def bfs(start, end, walls, limit=float('inf')):
	seen = set()
	q = [(0,start)]
	while q:
		steps, loc = q.pop(0)
		if loc == end:
			return steps
		if steps > limit:
			return None
		x, y = loc
		for dx,dy in ((1,0),(0,1),(0,-1),(-1,0)):
			nx, ny = x+dx, y+dy
			if (nx,ny) not in seen and (nx,ny) not in walls:
				q.append((steps+1,(nx,ny)))
				seen.add((nx,ny))
	return None

if __name__ == "__main__":

	# Part 1 Solution
	start = None
	end = None
	walls = set()
	x_dim = None
	y_dim = None
	with open("day20_input", "r") as infile:
		y = 0
		for line in infile:
			x_dim = len(line.strip())
			for x, char in enumerate(line.strip()):
				if char == '#': walls.add((x,y))
				elif char == 'S': start = (x,y)
				elif char == 'E': end = (x,y)
			y = y + 1
	y_dim = y

	normal_route = bfs(start, end, walls)

	found_cheats = 0

	for tx in range(x_dim-2):
		for ty in range(y_dim):
			if (tx, ty) not in walls and (tx+1 ,ty) in walls and (tx+2, ty) not in walls:
				new_walls = {*walls}
				new_walls.discard((tx+1,ty))
				path = bfs(start, end, new_walls, limit=normal_route-100)
				if path != None:
					found_cheats += 1
	for tx in range(x_dim):
		for ty in range(y_dim-2):
			if (tx, ty) not in walls and (tx ,ty+1) in walls and (tx, ty+2) not in walls:
				new_walls = {*walls}
				new_walls.discard((tx,ty+1))
				path = bfs(start, end, new_walls, limit=normal_route-100)
				if path != None:
					found_cheats += 1
	print(found_cheats)
	# Part 2 Solution

