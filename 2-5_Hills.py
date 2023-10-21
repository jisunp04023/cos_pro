def solution(arr):
	length = []
	
	for i in range(len(arr)):
		idx = i
		cnt = 1
		
		while True:
			if idx > len(arr) - 2:
				break
				
			a = arr[idx]
			b = arr[idx + 1]
			
			if a >= b:
				break
			
			else:
				cnt += 1
				idx += 1
				
		length.append(cnt)
		
	return max(length)


arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
