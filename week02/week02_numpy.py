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

