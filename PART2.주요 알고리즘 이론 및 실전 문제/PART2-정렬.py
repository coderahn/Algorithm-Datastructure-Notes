###정렬###

'''
정렬 알고리즘은 이진 탐색의 전처리 과정.
선택정렬, 삽입정렬, 퀵정렬, 계수정렬만 우선적으로 학습
'''

##1.선택정렬

#선택정렬예제(동빈북 159p)

'''
-선택정렬은 O(N^2) 시간복잡도
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)

##2.삽입정렬

#삽입정렬예제(동빈북 164p)

'''
-삽입정렬의 시간복잡도는 O(N^2)
-그러나 어느정도 정렬이 되어 있으면 최대 O(N) 시간복잡도가 나옴
-어느정도 정렬된 상태에서는 퀵정렬보다 빠름
'''

array2 = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array2)):
  for j in range(i, 0, -1):
    if array2[j] < array2[j-1]:
      array2[j],array2[j-1] = array2[j-1],array2[j]
    else:
      break

print(array2)

##3.퀵정렬

#퀵정렬예제(동빈북 168p)

'''
-퀵정렬 최대 O(NlogN)
-퀵정렬은 어느정도 정렬되어 있을 때 비효율(O(n^2))
'''

#퀵정렬 일반방법
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array[pivot] > array[left]:
      left += 1
    while right > start and array[pivot] < array[right]:
      right -= 1

    if left < right:
      array[left],array[right] = array[right],array[left]
    else:
      array[pivot],array[right] = array[right],array[pivot]

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)

print(array)

#파이썬 스타일 퀵정렬 방법
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)  

print(quick_sort(array))

##4.계수정렬

#계수정렬예제(동빈북 174p)

'''
-시간 복잡도 O(N+K)
-array의 max값 + 1만큼의 리스트를 선언
-데이터가 [0,99999] 이런식으로 있을 떄, 비효율성 초래
-동일값이 여러 개 있을 때 유용
-데이터 크기가 한정되어 있어야함(1000만개 미만)
'''

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#array의 최대값 + 1만큼의 카운트 리스트를 만든다.
count = [0] * (max(array) + 1)

#array값을 카운트의 인덱스로 하여, +1씩 증가
for i in array:
  count[i] += 1

#count를 돌면서 그 값만큼 반복하여 출력
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

##5.파이썬 라이브러리

'''
-sorted(), sort()
-항상 O(NlogN) 보장
'''
#sorted()
array = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)

#sort()
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

#key매개변수로 정렬 기준 만들기
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(array, key=setting)
print(result)

'''
출력
[('바나나', 2),('당근', 3),('사과', 5)]
'''

##<실전문제 : 위에서 아래로>

#<내풀이-선택정렬>
n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

for i in range(len(arr)):
  max_index = i
  for j in range(i+1, len(arr)):
    if arr[max_index] < arr[j]:
      max_index = j
  arr[i], arr[max_index] = arr[max_index], arr[i]

print(arr)

#<내풀이-삽입정렬>
n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

for i in range(1,len(arr)):
  for j in range(i, 0, -1):
    if arr[j] > arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else:
      break

print(arr)

#<내풀이-정렬 라이브러리>
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
  print(i, end=' ')


##<실전문제 : 성적이 낮은 순서로 학생 출력하기(동빈북 180p)>

#<내풀이-파이썬라이브러리>
n = int(input())
arr = []
for i in range(n):
  arr.append(input().split())

# def key_sort(arr):
#   return arr[0]
# arr.sort(key=key_sort)

#람다사용
arr.sort(key=lambda student: student[1])

'''
입력
2
홍길동 95
이순신 77
출력
이순신 홍길동
'''

for i in arr:
  print(i[0], end= ' ')


#<실전문제 : 두 배열의 원소 교체(동빈북 182p)>
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

print(a,b)

for i in range(k):
  if a[i] < b[i]:
    a[i],b[i] = b[i],a[i]
  else:
    break

print(sum(a))

'''
입력
5 3
1 2 5 4 3
5 5 6 6 5
출력
26
'''
