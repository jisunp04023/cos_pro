def solution(s1, s2):
	if len(s1) < len(s2):
		l = len(s1)
	else:
		l = len(s2)
	
	same1 = 0
	same2 = 0
	
	for i in range(l, 0, -1): # 5,4,3,2,1
		if s1[len(s1) - i :] == s2[: i]:
			same1 = i
			break
	
	for i in range(1, 0, -1):
		if s2[len(s2) - i :] == s1[: i]:
			same2 = i
			break
			
	answer = max(same1, same2)
	
	return len(s1) + len(s2) - answer


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")
