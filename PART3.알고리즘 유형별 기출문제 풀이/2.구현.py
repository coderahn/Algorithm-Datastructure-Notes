###구현 문제###

##07.럭키 스트레이트

#내풀이
n = input()

a = n[0:(len(n)//2)]
b = n[(len(n)//2):]

resultA = 0
resultB = 0
for i in range(len(n)//2):
  resultA += int(a[i])
  resultB += int(b[i])

if resultA == resultB:
  print('LUCKY')
else:
  print('READY')
  
#책풀이
'''
-result변수를 1개로 활용
'''
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i])
for i in range(length // 2):
  summary -= int(n[i])
  
if summary == 0:
  print('LUCKY')
else:
  print('READY')
  
'''
입력
123402
출력
LUCKY
'''

##08.문자열 재정렬

#내풀이
n = input()
alphabet = []
number = 0
for i in n:
  if ord(i) >= 65 and ord(i) <=90:
    alphabet.append(i)
  else:
    number+=int(i)
    
alphabet.sort()

result = ''
for i in alphabet:
  result += i
  
result += str(number)

print(result)

#책풀이

'''
-알파벳 여부는 간단하게 isAlpha()함수 사용
-리스트를 문자열로 변환시 join()함수 사용
'''
data = input()
result = []
value = 0

for x in data:
  #알파벳인 경우
  if x.isAlpha():
    result.append(x)
  #숫자인 경우
  else:
    value += int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))
  
#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

'''
입력1
K1KA5CB7
출력1
ABCKK13
입력2
AJKDLSI412K4JSJ9D
출력2
ADDIJJJKKLSS20
'''