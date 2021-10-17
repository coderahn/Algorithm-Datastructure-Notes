'''1)파이썬의 기타 연산자'''

#조건부 표현식(Conditional Expression) : if else를 한 줄에

#일반적 방법
score = 85
result = ""
if score >= 80:
  result = "Success"
else:
  result = "Fail"
print(result)

#조건부 표현식 방법
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

#리스트에서 특정한 원소값 없애는 일반적 방법(3,5 없애기)
a = [1,2,3,4,5,5,5]
removeData = {3,5}
result = []

for i in a:
  if i not in removeData: #i in removeData로 remove하는 방식은 a가 1씩 줄기 때문에 마지막 체크를 못함
    result.append(i)
else:
  print(result)    

#리스트에서 특정한 원소값 없애는 조건부 표현식 방법
a = [1,2,3,4,5,5,5]
removeData = {3,5}
result = [i for i in a if i not in removeData]
print(result)