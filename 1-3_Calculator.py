# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def func_a(numA, numB, exp):
	if exp == '+':
		return numA + numB
	elif exp == '-':
		return numA - numB
	elif exp == '*':
		return numA * numB

def func_b(exp):
	for index, value in enumerate(exp):
		if value == '+' or value == '-' or value == '*':
			return index

def func_c(exp, idx):
	numA = int(exp[:idx])
	numB = int(exp[idx + 1:])
	return numA, numB
