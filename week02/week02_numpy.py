#numpy는
#third party library다. (별도의 설치가 필요, 단 colab에서는 기본 설치가 되어 있음)
#python에서 수치 계산을 위한 핵심 라이브러리. 다차원 배열 객체와 이를 다루기 위한 다양한 함수를 제공.

import numpy as np

#zeros 함수
#zeros = np.zeros((3,4))
#zeros = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]], dtype=float)


#다 채워서 넣는 방법
#ones = np.ones((3,5))
#ones = np.array([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], dtype=float)

#print(zeros)
#print(ones)


#구간 배열 (증감식)(array range)
#0에서 20까지 2씩 증가
#range_array = np.arange(0, 20, 2)

#1에서 10까지 1씩 증가
#range_array = np.arange(1, 10)

#range_array = list()
#for i in range(1, 10):
#    range_array.append(i)

#print(range_array)


#구간 설정 2번째
#space_array = np.linspace(0, 1, 5) # 0부터 1까지 숫자 5개로 구간 설정
#print(space_array)

#space_array = np.linspace(0, 100, 5) # 0부터 100까지 숫자 5개로 구간 설정
#print(space_array)

