# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from pprint import pprint

def solution(bishops):
	board = [[0 for i in range(8)] for j in range(8)]

	
	move = [[1, -1], [1, 1], [-1, -1], [-1, 1]]
	
	# [row][col]
	for i in bishops:
		row = int(i[1]) # 1-8
		col = ord(i[0]) - 64
		
		board[row - 1][col - 1] = 1
		  
		for j in move:
				nx, ny = row, col
				mx, my = j[0], j[1]
				
				while True:
					nx += mx
					ny += my
					
					if nx < 1 or nx > 8 or ny < 1 or ny > 8:
						break
					
					board[nx - 1][ny - 1] = 1
					
	cnt = 0
	
	for i in board:
		for j in i:
			if j == 0:
				cnt += 1
	
	return cnt


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")
