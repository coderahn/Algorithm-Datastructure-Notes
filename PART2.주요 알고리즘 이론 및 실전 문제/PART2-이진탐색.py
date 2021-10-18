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

#내풀이(동빈북 197p)
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

'''
입력
5
8 3 7 9 2
3
5 7 9
출력
no yes yes
'''