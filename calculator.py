class Calculator:
    def __init__(self, a, b): # 자동 실행되는 생성자
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

cal1 = Calculator(3, 1)
cal2 = Calculator(4, 2)
print(cal1.a)
print(cal1.b)
print(cal1.sub())
print(cal1.mul())

print(cal2.add())
print(cal2.div())

class BabyCalculator(Calculator): # Calculator의 기능을 모두 상속 받음
    def square(self): # a의 b승 계산하는 함수 추가
        return self.a ** self.b

    def div(self): # Calculator의 div 함수를 오버라이드함
        if not self.b:
            return 0
        else:
            return self.a / self.b

cal3 = BabyCalculator(6, 0)

print(cal3.square())
print(cal3.div())
