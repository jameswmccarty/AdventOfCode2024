#!/usr/bin/python

# Advent of Code 2024 Day 17

# 4A, 5B, 6C
regs = {4:None,5:None,6:None}

ip = 0

mem = []

def adv(operand):
	global regs
	if operand < 4:
		regs[4] = regs[4] // 2**operand
	else:
		regs[4] = regs[4] // 2**regs[operand]

def bxl(operand):
	global regs
	regs[5] ^= operand

def bst(operand):
	global regs
	if operand < 4:
		regs[5] = operand % 8
	else:
		regs[5] = regs[operand] % 8

def jnz(operand):
	global ip
	if regs[4] != 0:
		ip = operand - 2

def bxc(operand):
	global regs
	regs[5] = regs[5] ^ regs[6]

def out(operand):
	if operand < 4:
		print(operand % 8,end=',')
	else:
		print(regs[operand] % 8,end=',')

def bdv(operand):
	global regs
	if operand < 4:
		regs[5] = regs[4] // 2**operand
	else:
		regs[5] = regs[4] // 2**regs[operand]

def cdv(operand):
	global regs
	if operand < 4:
		regs[6] = regs[4] // 2**operand
	else:
		regs[6] = regs[4] // 2**regs[operand]

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

if __name__ == "__main__":

	# Part 1 Solution
	with open("day17_input_test", "r") as infile:
		for line in infile:
			if "Register A:" in line:
				regs[4] = int(line.lstrip("Register A: ").strip())
			if "Register B:" in line:
				regs[5] = int(line.lstrip("Register B: ").strip())
			if "Register C:" in line:
				regs[6] = int(line.lstrip("Register C: ").strip())
			if "Program:" in line:
				mem = [*map(int,line.lstrip("Program: ").strip().split(','))]

	print(regs, mem)

	while ip < len(mem):
		opcode, operand = mem[ip], mem[ip+1]
		opcodes[opcode](operand)
		ip += 2
	# Part 2 Solution
