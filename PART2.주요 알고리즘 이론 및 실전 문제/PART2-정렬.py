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

##퀵정렬예제(동빈북 168p)

##계수정렬예제(동빈북 174p)

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
