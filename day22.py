#!/usr/bin/python

# Advent of Code 2024 Day 22

def rng(seed):
	while True:
		seed = ((seed * 64) ^ seed) % 16777216
		seed = ((seed//32) ^ seed) % 16777216
		seed = ((seed * 2048) ^ seed) % 16777216
		yield seed

if __name__ == "__main__":

	# Part 1 Solution
	total = 0
	with open("day22_input", "r") as infile:
		for line in infile:
			a = rng(int(line.strip()))
			for _ in range(2000):
				b = next(a)
			total += b
	print(total)

	# Part 2 Solution


