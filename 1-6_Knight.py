def alphatonum(alpha):
	if alpha == 'A':
		return 1
	if alpha == 'B':
		return 2
	if alpha == 'C':
		return 3
	if alpha == 'D':
		return 4
	if alpha == 'E':
		return 5
	if alpha == 'F':
		return 6
	if alpha == 'G':
		return 7
	if alpha == 'H':
		return 8
	
def move(x, y):
	return [[x+2, y-1], [x+2, y+1], [x-2, y-1], [x-2, y+1],
				 [x+1, y-2], [x-1, y-2], [x+1, y+2], [x-1, y+2]]
	
	
def solution(pos):
	answer = 0
	
	row = int(pos[1]) # 가로
	col = alphatonum(pos[0]) #세로
	
	for i in move(row, col):
		if i[0] > 0 and i[0] < 9 and i[1] >0 and i[1] < 9:
			answer += 1
	
	return answer


pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")
