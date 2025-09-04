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

#---------------------------------

#arr = np.array(["korean", "english", "mathmatics"])
#print(arr.shape, arr.dtype, arr.ndim, arr.size)
#----> (3,) <U10 1 3

#arr = np.array([[1, 2, 3], [4, 5, 9]])
#print(arr.shape, arr.dtype, arr.ndim, arr.size)
#----> (2, 3) int64 2 6

#arr = np.array(
#    [
#        [
#            [1.0 , 2.0, 3.1],
#            [4.2 , 5.9, 9.1]
#        ],
#        [
#            [1.1, 0.8, 2.1],
#            [6.3, 1.9, 77.1]
#        ]
#    ]
#)
#print(arr.shape, arr.dtype, arr.ndim, arr.size)
# ----> (2, 2, 3) float64 3 12


#3차원 배열에서 1.9만 출력--------------
# ----> (2, 2, 3) float64 3 12
# arr = np.array(
#    [
#        [ #0
#            [1.0 , 2.0, 3.1], #0
#            [4.2 , 5.9, 9.1] #1
#        ],
#        [ #1
#            [1.1, 0.8, 2.1], #0
#            [6.3, 1.9, 77.1] #1
#        ]
#    ]
# )
# print(arr[1, 1, 1])
#3차원 배열에서 1.9만 출력---------------



#----------------------------------------------------------------

# arr = np.arange(1, 6)
#
# #indexing
# print(arr[2])
# print(arr[4], arr[-1])
#
# #slicing
# print(arr[1:3]) # [2 3]
# print(arr[:3]) # [2 3]
# print(arr[:3]) # [1 4]

#----------------------------------------------------------------
# 2d 배열
# arr2d = np.array(
#     [
#         [3, 2, 1],
#         [4, 5, 6],
#         [14, -5, 76]
#     ]
# )
# print(arr2d)
# print(arr2d[1, 2])  # 6
# print(arr2d[:, 1])  # [2  5 -5] 모든 행의 1열(0열~2열)

#----------------------------------------------------------------
#산술 연산

# a=np.array([3,2,1])
# b=np.array([6,5,4])
#
# print(a+b)
# print(a*b)
# print(a**2)
# print(a+10)
# print(b*2)

#----------------------------------------------------------------

# c = np.arange(1, 13)  # 1차원 배열
#
# # r = c.reshape(2, 2, 3)  # 3차원 배열형태로 변환
# r = c.reshape(4, 3)  # 2차원 배열형태로 변환
# print(c)
# print(r)
# f = r.flatten()  # 2차원 배열을 1차원 배열로 변환
# print(f)
#
# # 전치행렬
# t = r.T
# print(t)
#
# # 단위행렬
# e1 = np.eye(4)
# print(e1)

#---------------------------------------------------------------

# d = np.array([4, 25, 9, 16])
#
# print(np.sqrt(d))  # 제곱근 square root
# print(np.exp(d))  # 지수함수 exponent function
# print(np.log(d))  # 자연로그
#
# e = np.array([0, np.pi/2, np.pi])  # [0, 3.14159265/2, 3.14159265]
# print(e)
# print(np.sin(e))  # 사인함수
# print(np.cos(e))  # 코사인함수

#--------------------------------------------------------------

# g = np.array([
#     [3, 2, 1],
#     [6, 5, 4]
# ])
# print(np.sum(g))
# print(np.sum(g, axis=0))  # 열 기준을 축으로 더함
# print(np.sum(g, axis=1))  # 행 기준을 축으로 더함
#
# print(np.mean(g))  # 산술평균  21/6
# print(np.max(g))
# print(np.min(g))
# print(np.std(g))  # 표준편차 standard deviation

#----------------------------------------------------------------

# # 조건부 선택과 필터링
# h = np.arange(1, 6)
#
# mask = h > 2
# print(h[mask])
#
# result = np.where(h > 3, h, 0)  # 3보다 큰 값은 그 값 그대로 3이하의 값은 0으로 처리
# print(result)

#----------------------------------------------------------------

# np.random.seed(50)  # 시드 설정
#
# x = np.random.random(5)  # 0 ~ 1 사이의 실수 5개 랜덤 추출
# print(x)
# y = np.random.randint(1, 10, 5)  # 1 ~ 9 사이의 정수 5개 랜덤 추출
# print(y)
# z = np.random.normal(0, 1, 5)  # 정규분포
# print(z)
#
# # q = np.arange(1, 6)
# # choice = np.random.choice(q, 3)
# # print(choice)
#
# q = np.array(["가위", "바위", "보"])
# choice = np.random.choice(q, 2)
# print(choice)