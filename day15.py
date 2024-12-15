#!/usr/bin/python

# Advent of Code 2024 Day 15

walls = set()
move_deltas = {'^': (0,-1), '>': (1,0), '<':(-1,0), 'v': (0,1)}
x_dim, y_dim = 0, 0

class Box:

	boxes = dict()

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.boxes[(x,y)] = self

	def gps(self):
		return self.x + 100*self.y

	def move_by(self, dx, dy):
		nx, ny = self.x + dx, self.y + dy
		if (nx, ny) in walls:
			return False
		if (nx, ny) in Box.boxes:
			if Box.boxes[(nx, ny)].move_by(dx, dy):
				t = Box.boxes.pop((self.x, self.y))
				self.x = nx
				self.y = ny
				Box.boxes[(nx, ny)] = t
				return True
			return False
		t = Box.boxes.pop((self.x, self.y))
		self.x = nx
		self.y = ny
		Box.boxes[(nx, ny)] = t
		return True

def print_state(pos):
	print("Bot pos",pos)
	for y in range(y_dim):
		for x in range(x_dim):
			if (x,y) in walls: print('#', end='')
			elif (x,y) in Box.boxes: print('O',end='')
			elif (x,y) == pos: print('@',end='')
			else: print('.',end='')
		print()
	print()

if __name__ == "__main__":

	# Part 1 Solution
	bot = None
	moves = ''
	y = 0
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			if any(c in line for c in '<v>^'):
				moves += line.strip()
			elif len(line.strip()) > 0:
				x_dim = len(line.strip())
				for x, char in enumerate(line.strip()):
					if char == '#': walls.add((x, y))
					elif char == 'O': Box(x, y)
					elif char == '@': bot = (x, y)
				y += 1
	y_dim = y

	for move in moves:
		#print("Move",move)
		#print_state(bot)
		x, y = bot
		dx, dy = move_deltas[move]
		nx, ny = x+dx, y+dy
		if (nx, ny) not in walls and (nx, ny) not in Box.boxes:
			bot = (nx, ny)
		elif (nx, ny) not in walls and (nx, ny) in Box.boxes:
			if Box.boxes[(nx, ny)].move_by(dx, dy):
				bot = (nx, ny)
	print(sum(box.gps() for box in Box.boxes.values()))

	# Part 2 Solution
