###그리디###

##2.큰수의법칙(동빈북 92P)

#<내 풀이>
#입력
n,m,k = map(int, input().split())
arr = list(map(int,input().split()))

#정렬
arr.sort(reverse=True)

#로직 작성
sum = 0
cnt = 0
pointer = 0
for i in range(m):
  sum+=arr[pointer]
  cnt+=1

  #포인터가 한번 증가한 상태인경우
  if pointer != 0:
    #증가한 포인터와 첫번째 포인터 값이 다른 경우(뒤에가 무조건 작은 경우)
    if arr[pointer] != arr[pointer - 1]:
      #포인터를 초기화(가장 큰 수를 더하기)
      pointer = 0
      cnt = 0

  if (cnt == k):
    pointer += 1
    cnt = 0
else:
  print(sum)

#arr[0]을 sum에 더하면서 cnt를 증가시킨후, cnt가 k와 같을 때 arr[1]을 위한 pointer를 증가시키고, cnt를 0으로 초기화
#arr[1]을 더하고난 후, 바로 가장 최대값인 arr[0]으로 더하기 위해 그 작업을 중간에 해준다. 
#arr[0]과 arr[1]이 같으면, 바로 arr[0]으로 돌아갈 수 있게 pointer를 0으로 초기화하고 cnt도 0으로 초기화한다.
#if arr[pointer] != arr[pointer - 1]: -> 이조건이 없어도 결과는 같은듯 하다. [0]과 [1]이 같으면 그냥 앞에꺼를 더하든 두번째꺼를 더하든 같기 때문에 초기화만 해주면 어떤 경우도 포함한다.

#<동빈북 풀이1>
#이중 반복문이지만 절차지향으로 가독성 좋게 푼 것 같다.
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  #최대값더하기 반복
  for i in range(k):
    if m == 0:
      break
    result += first
    m-=1
  if m == 0:
    break
  result += second
  m-=1
  
print(result)

#<동빈북 풀이2>
#갓갓..반복되는 패턴이 있음. 6,6,6,5   6,6,6,5 ...
#6,6,6,5로 반복되는 수열
#k+1은 반복되는 수열의 길이(4)
#m을 k+1로 나누면 반복되는 수열의 횟수(2)
#나눌 때 꼭 짝수로 떨어지지 않을 수 있음. 나머지연산자로 +1을 해줄 수도 있음
#이 횟수에 k를 곱하면 가장 큰 수의 반복 갯수(6)
#가장큰값을 반복갯수(6)으로 곱하고, 나머지는 second를 더하면됨

n,m,k=map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1))
count += m % (k + 1)

result = 0
result += count * first 
result += (m-count) * second

print(result)

##3.숫자카드게임(동빈북 96P)

#<내풀이>
#min()을 왜 안썼지..

#input
n,m = map(int,input().split())

#정렬
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr2 = []
for i in range(n):
  arr[i].sort()
  arr2.append(arr[i][0])

print(max(arr2))

#<동빈북 풀이1>
n, m = map(int,input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

#<동빈북 풀이2>
n, m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  
  result = max(result, min_value)
  
print(result)

##4.1이 될 때까지(동빈북 99P)

#<내풀이>
n,k = map(int, input().split())
cnt = 0
while True:
  cnt+=1
  if n%k == 0:
    n = n//k
  else:
    n = n-1
  
  if n == 1:
    break

print(cnt)

#<동빈북 풀이1>

n,k = map(int, input().split())
result = 0

while n>=k:
  while n%k!=0:
    n-=1
    result+=1
  n//=k
  result+=1

while n>1:
  n-=1
  result+=1

print(result)

#<동빈북 풀이2>
n,k = map(int, input().split())
result = 0

while True:
  #빼는 수를 한 번에 구할 수 있는 방법
  target = (n//k)*k
  result += (n-target)
  n = target

  if n < k:
    break
  result += 1
  n//=k

result += (n-1)
print(result)