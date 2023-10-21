# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(commands):
	move = [[-1, 0], [1, 0], [0, 1], [0, -1]] # 순서대로 L R U D
	answer = [0, 0]
	
	for i in commands:
		if i == 'L':
			answer[0] += move[0][0]
			answer[1] += move[0][1]
		if i == 'R':
			answer[0] += move[1][0]
			answer[1] += move[1][1]
		if i == 'U':
			answer[0] += move[2][0]
			answer[1] += move[2][1]
		if i == 'D':
			answer[0] += move[3][0]
			answer[1] += move[3][1]
			
	return(answer)
	


commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")
