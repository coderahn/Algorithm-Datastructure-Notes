#함수 호출 시 인자를 넘겨줄 때 파라미터 변수를 직접 지정 가능
def add(a, b):
  print('함수의 결과:', a - b)
add(b=3, a=7) #4

#global 키워드 : 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우
a = 0

def func():
  global a #a를 전역변수로 사용함을 명시
  a += 1

for i in range(10):
  func()

print(a) #10

#람다표현식 : 함수표현 간단하게
#1)더하기
print((lambda a,b:a+b)(1,2))

#2)map으로 리스트 매핑
a = map(lambda x:x*10, range(5))
print(list(a)) #[0,10,20,30,40]