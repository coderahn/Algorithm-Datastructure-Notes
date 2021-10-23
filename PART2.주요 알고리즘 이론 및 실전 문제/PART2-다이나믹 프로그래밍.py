###다이나믹 프로그래밍(DP)###

'''
-DP를 이용하여 피보나치 수열을 해결할 수 있음
-피보나치 수열은 재귀식을 이용할 수 있음 ex) fn(5) = fn(4) + fn(3)
-시간복잡도는 O(2^N)
-fn(100)이면 O(2^100)으로 계산 불가
-메모이제이션 기법으로 이미 계산된 것을 메모리에 담아두어 꺼내 사용할 수 있음
-DP를 사용하기 위한 조건
  1)큰 문제를 작은 문제로 나눌 수 있음
  2)작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일  
-DP의 2가지 방식
  1)탑다운 방식(재귀함수)
  2)보텀업 방식(반복문)
'''

##예제 8-2.메모이제이션 기법을 사용한 피보나치 수열(탑다운 방식)
#메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(n):
  if n == 1 or n == 2:
    return 1

  #계산한적 있는 문제면 그대로 반환
  if d[n] != 0:
    return d[n]

  #아직 계산한 적 없는 문제면 점화식에 따라 피보나치 결과 반환
  d[n] = fibo(n-1) + fibo(n-2)
  return d[n]

print(fibo(99))

##예제 8-4.메모이제이션 기법을 사용한 피보나치 수열(보텀업 방식)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
  d[i] = d[i-1] + d[i-2]

print(d[n])


'''
-문제풀 때, 일단 재귀함수로 단순 방식으로 푼 후, 메모이제이션을 적용하는 식으로 개선하는 것도 방법
-가능하면 탑다운 방식보다 보텀업 방식으로 구현하는 것을 권장. 시스템상 재귀함수 스택 크기가 한정되어 있을 수 있음


'''