# shallow copy, deep copy

#1.
a = [1, [3, -9], 4]

#modified (원본을 바꿈)
#a[1][0] = 55

import copy

b = a
c = a.copy()
d = a[:]
e = copy.deepcopy(a)
b[1][0] = 55

print(a) #본 복사
print(b) #본 복사
print(c) #얕은 복사
print(d) #얕은 복사
print(e) #깊은 복사

#2. https://pythontutor.com/ 체크해봐용


