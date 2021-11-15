###그래프 이론###

'''
[INTRO]
-코테에서 출제 비중은 낮지만 알아둬야할 그래프 관련 이론
-서로소 집합 자료구조, 신장트리 알고리즘(크루스칼 알고리즘),위상정렬
[앞내용 복습]
-다익스트라 최단 경로 알고리즘은 우선순위 큐 자료구조 사용 / 그래프 구현 방법 중 '인접 리스트' 방식 사용
-플로이드 워셜 알고리즘은 다이나믹 프로그래밍 점화식 방식 사용 / 그래프 구현 방법 중 '인접 행렬' 방식 사용
-노드의 개수가 적은 경우 -> 플로이드 워셜 / 노드와 간선 개수가 많은 경우 -> 다익스트라
[서로소 집합]
-서로소 집합 : 공통 원소 없는 집합 ex) {1,2},{3,4}
-서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
-union, find 연산으로 조작 가능
-union : 2개 원소가 포함된 집합을 하나의 집합으로 합치는 연산
-find : 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산
-트리 자료구조 이용
'''

##10-1 예제.기본적인 서로소 집합 알고리즘

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  #루트 노드가 아니라면 루트노드를 찾을 때까지 재귀적 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수, 간선(union 연산)의 개수
v, e = map(int, input().split())
parent = [0] * (v + 1) #부모테이블 초기화

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i
  
#union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

#각 원소가 속한 집합을 출력
print('각 원소가 속한 집합: ', end ='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')

'''
입력
6 4
1 4
2 3
2 4
5 6
출력
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5
'''