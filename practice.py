# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "낮잠"
# is_adult = age>=3


# print("우리집 "+ animal + "의 이름은 " + name +"에요")
# hobby = "공놀이"
# print(animal+ "는 " + str(age) + "살이며, " +hobby+"을 아주 좋아해요")
# print(animal+ "는 " ,age, "살이며, " ,hobby,"을 아주 좋아해요")
# print("연탄이는 어른일까요? ", is_adult)


##### 2>
# station = "사당"
# print(station+"행 열차가 들어 오고 있습니다.")
# station = "신도림"
# print(station+"행 열차가 들어 오고 있습니다.")
# station = "인천공항"
# print(station+"행 열차가 들어 오고 있습니다.")

##### 3>
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) #2^3 = 8
# print(5%3) #나머지 구하기 2
# print(10%3) #1
# print(5//3) #1
# print(10//3) #3

##### 4>
# print(2+3*4) #14
# print((3+3) *4) #24
# number = 2+3+4 #9

# print(number) #9
# number = number +2 #11
# print(number)
# number %= 2 
# print(number)

##### 5>
# print(abs(-5)) #5
# print(pow(4,2)) #4^3 = 4*4 =16
# print(max(5,12)) #12
# print(min(44,12)) #12
# print(round(3.14)) #3
# print(round(4.99)) #5

# from math import *
# print(floor(4.99)) #내림, 4
# print(ceil(3.14)) #올림,4
# print(sqrt(16)) #제곱근,4

##### 6>
# from random import *

# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) #0.0 ~10.0  미만의 임의의 값 생성
# print(int(random()*10)) #0~10 미만의 임의의 값 생성
# print(int(random()*10)) #0~10 미만의 임의의 값 생성
# print(int(random()*10)) #0~10 미만의 임의의 값 생성

# print(int(random() *10)+1) #1~10 이하의 임의의값 생성
# print(int(random() *10)+1) #1~10 이하의 임의의값 생성
# print(int(random() *10)+1) #1~10 이하의 임의의값 생성
# print(int(random() *10)+1) #1~10 이하의 임의의값 생성
# print(int(random() *10)+1) #1~10 이하의 임의의값 생성
# print(int(random() *10)+1) #1~10 이하의 임의의값 생성

# print(int(random() *45) +1) #1~45 이하의 임의의값 생성
# print(int(random() *45) +1) #1~45 이하의 임의의값 생성
# print(int(random() *45) +1) #1~45 이하의 임의의값 생성
# print(int(random() *45) +1) #1~45 이하의 임의의값 생성
# print(int(random() *45) +1) #1~45 이하의 임의의값 생성
# print(int(random() *45) +1) #1~45 이하의 임의의값 생성

# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성
# print(randrange(1,46)) #1~45 이하의 임의의 값 생성

# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #1~45 이하의 임의의 값 생성

######7>문자열
# sentense = '나는 소년입니다.'
# print(sentense)
# sentense2 = "파이썬은 쉬워요"
# print(sentense2)
# sentense3 = """나는 소년이고, 파이썬은 쉬워요"""
# print(sentense3)

#####8> 슬라이싱 : 필요한 문자만 잘라서 사용하는 것
# jumin = "850920-1243556"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7번째 부터 끝까지

# print("뒤 7자리 : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#####9> 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# print(index)
# print(python.find("Java")) #find는 찾고자 하는 문자열이 없을 경우 -1 을 반환한다
# #print(python.index("Java")) #index는 찾고자 하는 문자열이 없을 경우 error를 발생시킨다.
# print("hi")

# print(python.count("n"))

##### 10> 문자열 포맷
# print("a", "b")
# print("a","b")

# #방법1
# print("나느 %d살입니다." %20)
# print("나는 %s를 좋아해요"%"파이썬")
# print("Apple 은 %c로 시작해요" %"A")
# # %s
# print("나는 %s살입니다." %20)

#print("나는 %s색과 %s색을 좋아해요"%("파란", "빨간"))

# 방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age =20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color ="빨간", age=20))

# 방법4(v3.6 이상~)
# age = 20
# color = "빨간"

# print(f"나는 {age}살이며, {color}색을 좋아해요")

##### 11> 탈출 문자자 
# \" , \' : 문장내에서 따옴표 출력
# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")

# #\\ : 문장내에서는 \ 의 역슬래쉬로 바뀐다.

# print("C:\\Users\\Nadocoding\\")

# \r : 커서를 맨 앞으로 이동

# print("Red Apple\rPine")

#\b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

##### Quiz> 

# url = "http://naver.com"
# my_str = url.replace("http://","") #규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙2
# # my_str[0:5] -> 0~5 직전까지 . (0,1,2,3,4)

# print(my_str)
# password = my_str[:3] + str(len(my_str))+str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))

##### 12> 리스트 []

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,20]
# print(subway)

# subway =["유재석", "조세호","박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

#지하철에 있는 사름을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇 명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# #print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

##### 12> 사전(dictionary)

cabinet = {3:"유재석", 100:"조세호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# #print(cabinet[5]) #없는 key로 값을 가져오려고 할때 에러 발생
# print(cabinet.get(5)) # get을 사용해 값을 가져올때는 없는 값이라도 에러를 발생하지 않음음
# print(cabinet.get(5, "사용가능"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #false

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력

# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear
# print(cabinet)

##### 13>Tuple

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# #menu.add("생선까스") #튜플은 값추가가 불가능하다.

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name, age, hobby)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

##### 14> 세트(집합): 중복안됨, 순서 없음

# my_set = {1, 2, 3,4,4}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합(java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# #합집합(java도 할 수 있거나, python을 할수 있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합(java는 할 수 있지만, python을 하루 없는 개발자)
# print(java - python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)


# #java를 잊었어요
# java.remove("김태호")
# print(java)

##### 15> 자료구조의 변경
# 커피숍
# menu = {"커피","우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

##### Quiz>

# from random import *
# users = range(1, 21) #1부터 20까지 숫자를 생성
# print(type(users))
# users = list(users)
# # print(type(users))
# print(users)

# shuffle(users)
# print(users)

# winners = sample(users, 4)

# print("-- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다. --")


##### 16> IF문 ****

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈": 
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <=temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <=temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

##### 17> 반복문
# 1. for
# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")
# for wating_no in [0, 1, 2, 3, 4]:
#     print("대기번호 ; {0}".format(wating_no))
# for wating_no in range(1,6):
#     print("대기번호 ; {0}".format(wating_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]

# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# 2. While
# customer = "토르"
# index = 5
# while index>=1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer, index))
#     index +=1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# 3. continue 와 break

# absent = [2,5] #결석
# no_book = [7] #책을 깜빡했음
# for student in range(1, 11): #1~10번
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어줘".format(student))

# 4. 한줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 --> 101, 102, 103, 104,
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생 이름을 길이로 반환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 반환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

##### Quiz
# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 52): # 1~50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15:
#         print("[0] {0} 번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[] {0}번째 손님 (소요시간: {1}분)".format(i, time))
# print("총 탑승 승객 : {0} 분".format(cnt))


##### 18> 함수 ************
# 1. 사용법
# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")

# def deposit(balance, money): #입금
#     print("입금이 완료 되엇습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print("출금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance -money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money): #저녘에 출금
#     commission = 100 #수수료 100원
#     return commission, balance -money - commission



# balance = 0 #잔액
# balance = deposit(balance, 1000)
# # balance= withdraw(balance, 2000)
# # balance = withdraw(balance,  500)

# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 2. 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")

# 3. 키워드 값 : 키워드에 기본값 설정 시 순서가 뒤바뀌어도 상관없다.
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name= "김태호")

# 4. 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift")


##### 19> 지역변수와 전역변수
# gun = 10

# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun 을 사용하겠다.
#     gun = gun -soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun -soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# #checkpoint(2) # 2명이 경계근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

##### Quiz

# def std_weight(height, gender): # 키는 m 단위 (실수), 성별 "남자" / "여자"
#     if gender =="남자":
#         return height*height*22
#     else:
#         return height*height*21
    
# height = 164 # cm 단위
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)

# print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


##### 20> 표준 입출력
# import sys
# print("Python", "Java",file=sys.stdout)
# print("Python", "Java",file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


#은행 대기 순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
# print("입력하신 값은 " + answer + "입니다")
