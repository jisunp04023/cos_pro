def solution(arr, K):
	cnt = 0
	
	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			for k in range(j + 1, len(arr)):
				a = arr[i]
				b = arr[j]
				c = arr[k]
				
				if not (a + b + c) % K:
					cnt += 1
	
	return cnt


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
