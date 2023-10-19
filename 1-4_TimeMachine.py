def solution(num):
	answer = 0
	answer = num + 1
	
	while(True):
		if '0' in str(answer):
			answer += 1
			
		else:
			break
			
	return answer


num = 9949999;
ret = solution(num)
 
print("solution 함수의 반환 값은", ret, "입니다.")
