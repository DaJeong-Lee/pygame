#coding = utf-8
import math
x = math.sin(3)
print(x) # result is radian
#60분법 = radian * 180/파이
y = x * 180 / math.pi
print(y) # 60분법

t = math.tan(1.2490457723982544)
print(t)
print(t*180/math.pi)

at = math.atan(3)
print(at)

#카테시안 좌표계:

#각도를알고싶으면 아크탄젠트(숫자)를 넣어서 각도를 구할수있다.
x1 = 2
y1 = 1
x2 = 5
y2 = 5
#좌표 (x1,y1) (x2,y2) 이때 각 = math.atan2(y2-y1, x2-x1) this result is radian

angle = math.atan2(y2-y1, x2-x1)
print('angle is {} radian'.format(angle))
print('angle is {} dgree'.format(angle*180/math.pi))
