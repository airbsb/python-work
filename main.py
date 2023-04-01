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
 flag=True
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

#22
def fun22():
 mylist=[90,80,30,65]
 print(mylist.index(30))

#23
def fun23():
 mylist=[90,80,30,65]
 mylist2=[30,30,100]
 mylist=mylist+mylist2
 print(mylist)

#24
def fun24():
 mylist=[90, 80, 30, 65, 30, 30, 100]
 print(mylist.count(30))

#25
def fun25():
 mylist=[90, 80, 30, 65, 30, 30, 100]
 mylist.remove(30)
 print(mylist)

#26
def fun26():
 mylist=[90, 80, 30, 65, 30, 30, 100]
 index_65=mylist.index(65)
 del(mylist[index_65])
 print(mylist)

#27
def fun27():
 t1=(1,2,3)
 print(t1)

#28
def fun28():
 t1=(1,2,3)
 print(t1[:2])

#29
def fun29():
 t1=(30,)
 print(t1)

#30
def fun30():
 t1=(1,2)
 t2=("a","b")
 print(t1+t2)

#31
def fun31():
 t1=(1,2)
 print(t1*5)

#32
def fun32():
 dic={"name":"차혜진","age":22,"stdNum":202345050}
 print(dic)

#33
 dic["grade"]=1
 print(dic)

#34
 print(dic["name"])

#35
 print(dic.keys())

#36
 print(dic.values())

#37
 print(dic.items())

#38
 print("name" in dic)
 print("class" in dic)

#39
 del dic["grade"]
 print(dic)

#40
 dic.clear()
 print(dic)

#41
def fun41():
 a, b = input("두 수를 입력하세요.").split(" ")
 a=int(a)
 b=int(b)
 if(a>b):print(a)
 else:print(b)

#42
def fun42():
 num=int(input("20보다 작은 수를 입력하세요."))
 if (num>=20) : print("Too High")
 else : print("Thank you")

#43
def fun43():
 color=input("좋아하는 색을 입력하세요 : ")
 if(color.lower()=="red"):print("I like red too")
 else:print("I don't like that color, I prefer red")

#44
def fun44():
 mylist=[1,2,3,4,5]
 print(mylist)

#45
def fun45():
 total=0
 for i in range(1,11) : total+=i
 print(total)

#46
def fun46():
 lastnum=int(input("수를 입력해주세요."))
 total=0
 for i in range(1,lastnum+1) : total+=i
 print(total)

#47
def fun47():
 mylist=[]
 mylist=input("10가지 수를 입력해주세요.").split(",")

 for i in range(0,len(mylist)) : mylist[i]=int(mylist[i])

 mylist.sort(reverse=True)
 print("최대값 : ",mylist[0])
 print("최소값 : ",mylist[-1])

#48
def fun48():
 for i in range(1,6):
  print("*"*i)
  
#49
def fun49():
 a=input("python 을 입력하세요.")
 while a != "python":
  print("python 을 입력하세요.")
 print("good!")


fun49()
 