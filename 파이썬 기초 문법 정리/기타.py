##10진수 입력값 16진수(hex)로 출력하기(소문자)
a = int(input())
print('%x'%a)

##10진수 입력값 16진수(hex)로 출력하기(대문자)
b = int(input())
print('%X'%b) 

##16진수로 입력받아 8진수로 출력하기
c = input()
c = int(c,16) #입력값을 16진수로 인식해 변수 c에 저장
print('%o'%c)

##영문자를 십진수 유니코드로 출력하기(A->65)
d = ord(input())
print(d)

##정수를 유니코드로 출력하기(65->A)
e = chr(int(input()))
print(e)

##문자1개 입력받아 다음문자 출력
a = ord(input())+1
print(chr(a))
a = chr(ord(input())+1)
print(a)

##실수 1개 입력받아 소숫점 2번째 자리까지 반올림 값 출력
#1번방법
a = float(input())
print(round(a,2))
#2번방법(추천)
b = float(input())
print(format(b,'.2f'))

a,b = map(float, input().split())
#10.0 0.0001
#print(format(a/b,'.3f')) #round(a/b,3)으로 하면 100000.0이 나옴.

##round vs format
# 파이썬은 반올림을 하는 round() 함수를 내장하고 있습니다.
# 그러나 round() 함수는 끝자리가 0이면 출력을 하지 않는 문제가 있습니다.
# 예컨대 round(3.141592, 2)는 3.14를 출력하지만, round(3.101592, 2)는 3.1을 출력합니다.
# 참고로 올림 또는 내림을 하는 math.ceil과 math.floor은 정수만 반환합니다.
# 따라서 원하는 출력형식을 엄격하게 준수하려면 format() 함수를 사용해야 합니다.
# format() 함수는 format(item, 폭(width).정밀도(precision)f)의 형태로 사용하면 됩니다.
# 즉 format(3.141592, ".2f"))의 형식으로 소수점 두 자리까지 출력할 수 있습니다.
# 한편 "{:.1f}".format() 형태로도 사용할 수 있습니다.


##비트단위시프트연산자 <<, >>
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

##16진수 계산기
a = int(input(),16)
for i in range(1,16):
  print('%X'%a,'*%X'%i,'=%X'%(a*i),sep='')

##코드업(6082)
#3,6,9출력(박수는 X로, 33은 XX)
#리스트 자료형 등 전이기 때문에 문자,반복문만 사용하기
a = int(input())

for i in range(1, a + 1):
  tsn = str(i)
  three = tsn.count('3') #3개수 세기
  six = tsn.count('6') #6개수 세기
  nine = tsn.count('9') #9개수 세기

  result = three + six + nine #박수 반복을 위한 최종개수

  if (('3' in tsn) or ('6' in tsn) or ('9' in tsn)):
    clap = ''
    for _ in range(result):
      clap += 'X'
    else:
      print(clap, end=' ')
  else:
    print(i, end=' ')
#----------------------------------------------------------------------------------------    
#input : 33
#ouput : 1 2 X 4 5 X 7 8 X 10 11 12 X 14 15 X 17 18 X 20 21 22 X 24 25 X 27 28 X X X X XX 
#----------------------------------------------------------------------------------------