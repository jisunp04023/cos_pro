def solution(n):
    add = [1]
    key = 1
    p = 1

    while True:
        for j in range(2):
            key += (n - p) * 2
            add.append(key)
        if len(add) >= n:
            break
        p += 2

    answer = 0
    for i in range(n):
        answer += add[i]
    return answer


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
