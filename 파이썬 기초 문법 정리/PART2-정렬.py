###정렬###

'''
정렬 알고리즘은 이진 탐색의 전처리 과정.
선택정렬, 삽입정렬, 퀵정렬, 계수정렬만 우선적으로 학습
'''


##선택정렬예제(동빈북 159p)

#선택정렬은 O(N^2) 시간복잡도

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)

##삽입정렬예제(동빈북 164p)

#삽입정렬의 시간복잡도는 O(N^2)
#그러나 어느정도 정렬이 되어 있으면 최대 O(N) 시간복잡도가 나옴
#어느정도 정렬된 상태에서는 퀵정렬보다 빠름

array2 = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array2)):
  for j in range(i, 0, -1):
    if array2[j] < array2[j-1]:
      array2[j],array2[j-1] = array2[j-1],array2[j]
    else:
      break

print(array2)