#1
def fun1():
 str=input("당신은 누구입니까? ")
 print("안녕", str)

#2
def fun2():
 print("안녕하세요.\n파이썬을 사용 중입니다.")

#3
def fun3():
 str="Hello"
 lag=True
 age=20
 score=[70,80,90] 
 student={"name":"JW","age":24}
 val=(10,)
 val2={1,2,3,2,1}
 print(type(str))
 print(type(flag))
 print(type(age))
 print(type(score))
 print(type(student))
 print(type(val))
 print(type(val2))

#4
def fun4():
 str="Hello"
 score=[70,80,90]
 student={"name":"JW","age":24}
 val=(10,)
 val2={1,2,3,2,1} 
 print(len(str))
 print(len(score))
 print(len(student))
 print(len(val))
 print(len(val2))

#5
def fun5():
 str="Hello Python"
 print(str[:5])
 print(str[6:])

#6
def fun6():
 year=input("출생년도를 입력하세요")
 age=input("나이")
 print("출생년도를 입력하세요 : ",year)
 print("나이 : ",age)
 print(f"당신은 {age}살 입니다.")

#7
def fun7():
 num=int(input("숫자를 입력하세요 "))
 if num%2==0 : print("짝수입니다.")
 else : print("홀수입니다.")

#8
def fun8():
 korean =int(input("국어점수를 입력하세요. "))
 english=int(input("영어점수를 입력하세요. "))
 math=int(input("수학점수를 입력하세요. "))
 my_list=[korean,english,math]
 s=sum(my_list)
 avg=s/3
 print(avg)

#9
def fun9():
 He=input("첫 번째 문자열을 입력하세요: ")
 llo=input("두 번째 문자열을 입력하세요: ")
 print(He+llo)

#10
def fun10():
 str=input("문자열을 입력하세요: ")
 num=int(input("반복횟수를 입력하세요: "))
 for i in range(num) : print(str)

#11
def fun11(): 
 ramyeon,snack,drink=input("라면, 과자, 음료의 구매 개수를 입력해주세요 : ").split(",")
 total=int(ramyeon)*1000+int(snack)*800+int(drink)*1500
 print("총 금액은 %s 원 입니다." % total)

#12
def fun12():
 print(5%3)

#13
def fun13():
#num1=num1+3
 num1=0
 num1+= 3
 print(num1)

#14
def fun14():
 a=int(input("첫 번째 수 : "))
 b=int(input("두 번째 수 : "))
 print("더하기: ",a+b)
 print("빼기: ",a-b)
 print("곱하기: ",a*b)
 print("나누기: ",a/b)
 print("몫: ",a//b)
 print("나누기: ",a%b)
 print("제곱: ",a**b)

#15
def fun15():
 mylist=[65,80,55]
 print(mylist)

#16
def fun16():
 mylist=[65,80,55]
 print(mylist[1])

#17
def fun17():
 mylist=[65,80,55]
 mylist.append(100)
 print(mylist)

#18
def fun18():
 mylist=[65,80,55,100]
 mylist[3]=90
 print(mylist)

#19
def fun19():
 mylist=[65,80,55,90]
 mylist.sort()
 print(mylist)
 mylist.sort(reverse=True)
 print(mylist)

#20
def fun20():
 mylist=[65,80,55,90]
 mylist.insert(2,30)
 print(mylist)

#21
def fun21():
 mylist=[90,80,30,65,55]
 print(mylist[-1])
 mylist.pop()
 print(mylist)

fun21()
