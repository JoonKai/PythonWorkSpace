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

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다")

##### 21> 다양한 출력 포맷
# # 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 때 + 로 표시, 음수일 때 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리마다 콤마를 찍어보기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3))

##### 22> 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #List형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

##### 23>Pickle

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이:":30, "취미":["축구", "골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file 있는 정보를 proifle 에 불러오기
# print(profile)
# profile_file.close()

##### 24> With
# import pickle

# with open("profile.pickle", "rb") as profile_file: # with를 사용할 경우 with 문이 끝나면 자동으로 close 해줌줌
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

##### Quiz
# for i in range(1, 51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- "+str(i)+" 주차 주간보고 -")
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

##### 25> class ********************************

# 마린 : 공격 유닛
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 시저탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시" , damage)
# attack(tank_name, "1시", tank_damage)


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))




# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# # 1. __init__(생성자)
# # 2. 멤버변수
# # self.name 클래스 내에서 생성된 변수

# # 레이스 : 공증 유닛 , 비행기 , 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 외부에서 사용가능

# # 마인드 컨트롤 : 상태방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) # 클래스 외부에서 변수를 확장해서 사용할 수 있음.

# 3. 메소드

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #  파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 4. 상속 *****
#메딕의 경우
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #  파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 5> 다중 상속

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
    
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# #  드랍쉽 : 공중유닛, 수송기, 공격 기능 없음
# class Flyalbe:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#               .format(name, location, self.flying_speed))
# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyalbe):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyalbe.__init__(self, flying_speed)

# # 발키리 : 공격유닛 , 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

##### 26> 메소드 오버라이딩

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# # 공격 유닛닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# #  드랍쉽 : 공중유닛, 수송기, 공격 기능 없음
# class Flyalbe:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#               .format(name, location, self.flying_speed))
# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyalbe):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0 으로 처리
#         Flyalbe.__init__(self, flying_speed)
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 : 지상유닛
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

##### 27> Pass
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# # 공격 유닛닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# #  드랍쉽 : 공중유닛, 수송기, 공격 기능 없음
# class Flyalbe:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#               .format(name, location, self.flying_speed))
# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyalbe):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0 으로 처리
#         Flyalbe.__init__(self, flying_speed)
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# 1. Pass

# 건물 
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단은 아무것도 안하고 넘어간다.

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛,
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass
# game_start()
# game_over()
# 2. super

#건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # 둘중 하나 가능한데 self를 제외하고 사용한다.
#         self.location = location

##### 실제 테스트
# from random import *

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# # 공격 유닛닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage

#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력{0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#               .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# #  드랍쉽 : 공중유닛, 수송기, 공격 기능 없음
# class Flyalbe:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#               .format(name, location, self.flying_speed))
# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyalbe):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0 으로 처리
#         Flyalbe.__init__(self, flying_speed)
#     def move(self, location):
#         self.fly(self.name, location)

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
#     # 스팀팩
#     def stimpack(self):
#         if self.hp >10:
#             self.hp -=10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#     #시즈모드 : 탱크 지상모드
#     seize_developed = False
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return 

#         #시즈모드가 아닐때
#         if self.seize_mode ==False:
#             print("{0} : 시즈모드로 전환합니다. ".format(self.name))
#             self.damage *=2
#             self.seize_mode = True
#         #시즈모드 일때때
#         else:
#             print("{0} : 시즈모드를 해제합니다.. ".format(self.name))
#             self.damage /=2
#             self.seize_mode = False

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False #클로킹 모드

#     def clocking(self):
#         if self.clocked == True: 
#             print("{0} : 클로킹 모드 해제합니다. ".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다. ".format(self.name))
#             self.clocked = True


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장 하셨습니다.")

# #실제 게임 시작
# game_start()

# #마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# #탱크 2기 생성

# t1 = Tank()
# t2 = Tank()

# #레이스 1기 생성
# w1 = Wraith()

# #유닛 일괄 관리(생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동

# for unit  in attack_units:
#     unit.move("1시")

# #탱크 시즈모드 개발

# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료 되었습니다.")

# #공격 모드 준비 ( 마리 : 스팀팩 , 탱크 : 시즈모드 , 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# #전군 공격

# for unit in attack_units:
#     unit.attack("1시")

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음(5~20)

# # 게임 종료

# game_over()
