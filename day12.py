#!/usr/bin/python

# Advent of Code 2024 Day 12

edges = dict()

def build_perim(points):
	edges = dict()
	for pt in points:
		x, y = pt
		e1 = ((x,y),(x+1,y))
		e2 = ((x,y),(x,y+1))
		e3 = ((x+1,y),(x+1,y+1))
		e4 = ((x,y+1),(x+1,y+1))
		for e in [e1,e2,e3,e4]:
			if e not in edges:
				edges[e] = 1
			else:
				edges[e] += 1
	return edges

def score_area(area, max_x, max_y):
	squares = len(area)
	perim = build_perim(area)
	boundary = sum( v for k,v in perim.items() if v==1)
	return boundary * squares

def segment_into_distinct(area):
	new_areas = list()
	while area:
		sub_area = set()
		loc = area.pop()
		sub_area.add(loc)
		q = [loc]
		while q:
			x, y = q.pop()
			for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
				nx, ny = x+dx,y+dy
				if (nx,ny) in area:
					area.remove((nx,ny))
					sub_area.add((nx,ny))
					q.append((nx,ny))
		if len(sub_area) > 0:
			new_areas.append(sub_area)
	return new_areas

	

if __name__ == "__main__":

	areas = dict()

	# Part 1 Solution
	with open("day12_input", "r") as infile:
		y = 0
		for line in infile:
			for x, c in enumerate(line.strip()):
				if c not in areas:
					areas[c] = set()
				areas[c].add((x,y))
			max_x = len(line.strip())
			y += 1
	max_y = y

	listed_areas = []
	for area in areas:
		for entry in segment_into_distinct(areas[area]):
			listed_areas.append(entry)
	print(sum(score_area(x, max_x, max_y) for x in listed_areas))
	# Part 2 Solution
