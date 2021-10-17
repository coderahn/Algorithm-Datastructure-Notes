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

