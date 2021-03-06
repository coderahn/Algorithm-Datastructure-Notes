###이진탐색(Binary Search)###

##<예제(재귀적 방식)>
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

#원소개수, 찾으려는 문자열
n,target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

##<예제(반복문 방식)>
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
    
#원소개수, 찾으려는 문자열
n,target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

##부품찾기

'''
정렬을 위한 시간복잡도 O(N * logN)
이진탐색을 위한 시간복잡도 O(M * logN)
총 시간복잡도 O((N+M) * logN)
'''

#이진탐색 방법
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binarySearch(arr, target, start, end):
  if start > end:
    return 0
  
  mid = (start + end) // 2

  if arr[mid] == target:
    return 1
  elif arr[mid] > target:
    return binarySearch(arr, target, start, mid-1)
  elif arr[mid] < target:
    return binarySearch(arr, target, mid+1, end) 
  else:
    return 0

for i in range(m):
  if 1== binarySearch(arr1, arr2[i], 0, n-1):
    print('yes', end= ' ')
  else:
    print('no', end= ' ')

#계수정렬 방법
n = int(input())
arr = list(map(int, input().split()))
count = [0] * (max(arr) + 1)

m = int(input())
findArr = list(map(int, input().split()))

for i in arr:
  count[i] += 1

print(count)  
for i in findArr:
  if count[i] != 0:
    print('yes', end=' ')
  else:
    print('no', end=' ')
'''
입력
5
8 3 7 9 2
3
5 7 9
출력
no yes yes
'''

##떡볶이 떡 만들기(동빈북 201p)

'''
파라메트릭 서치 유형(최적화문제를 결정문제로 바꾸어 해결하는 기법)
'''

#<책풀이>
n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
start = 0
end = max(arr)
result = 0
while start <= end:
  sum = 0
  mid = (start + end) // 2

  for i in arr:
    if i > mid:
      sum += (i-mid)

  if sum < m:
    end = mid - 1
  else:
    start = mid + 1
    result = mid

print(result)

#<내풀이(2회차)>
n,m = map(int, input().split())

arr = list(map(int, input().split()))
sum = 0

def binary_search(arr, target, start, end):
  global sum
  
  #손님이 원하는 떡 길이(target)과 절단된 떡의 합(sum)이 같지 않다면 반복
  while target != sum:
    sum = 0
    mid = (start + end) // 2
    
    #절단된 떡을 합치기
    for i in arr:
      if (i - mid) > 0:
        sum += (i - mid)
        
    if sum == target:
      return mid
    elif sum > target:
      start = mid + 1
    else:
      end = mid - 1
      
  return None

#end는 가장 긴 떡을 기준으로 이진탐색
result = binary_search(arr, m, 0, max(arr))

print(result)

'''
입력
4 6
19 15 10 17
출력
15
'''


