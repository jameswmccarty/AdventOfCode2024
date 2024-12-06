#!/usr/bin/python

# Advent of Code 2024 Day 06

if __name__ == "__main__":

	# Part 1 Solution
	obstacles = set()
	visited = set()
	path = []
	max_x = 0
	max_y = 0
	pos = None
	start = None
	dirs = [(0,-1),(1,0),(0,1),(-1,0)]
	going = 0
	turn_points = set()
	with open("day06_input", "r") as infile:
		y = 0
		for line in infile:
			max_x = len(line.strip())
			for x, char in enumerate(line.strip()):
				if char == '#':
					obstacles.add((x,y))
				if char == '^':
					pos = (x,y)
					start = pos
					visited.add(pos)
					path.append((x, y, 0))
			y += 1
		max_y = y

	while pos[0] >=0 and pos[0] < max_x and pos[1] >= 0 and pos[1] < max_y:
		x, y = pos
		next_x, next_y = x+dirs[going][0], y+dirs[going][1]
		while (next_x, next_y) in obstacles:
			turn_points.add((x,y))
			going += 1
			going = going % 4
			next_x, next_y = x+dirs[going][0], y+dirs[going][1]
		pos = (next_x, next_y)
		visited.add(pos)
		path.append((next_x, next_y, going))
	path.pop()
	visited.discard(pos)
	print(len(visited))

	# Part 2 Solution
	obs_points = set()
	for point in path:
		x, y, direction = point
		if (x, y) != start:
			new_obstacles = {*obstacles, (x, y)}
			pick_pos = (x, y)
			seen = set()
			pos = start
			going = 0
			while pos[0] >= 0 and pos[0] < max_x and pos[1] >= 0 and pos[1] < max_y:
				x, y = pos
				next_x, next_y = x+dirs[going][0], y+dirs[going][1]
				while (next_x, next_y) in new_obstacles:
					going += 1
					going = going % 4
					next_x, next_y = x+dirs[going][0], y+dirs[going][1]
				pos = (next_x, next_y)
				if (next_x, next_y, going) in seen:
					obs_points.add(pick_pos)
					break
				seen.add((next_x, next_y, going))
	print(len(obs_points))
