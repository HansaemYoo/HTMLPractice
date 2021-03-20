

'''Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
    예) http://naver.com
    조건1: http:// 부분제외 
    조건2: 점(.) 이후 부분 제외
    조건3: 남은 글자 중 처음 세자리 + 글자 수 + 글자내 'e' 수 + !로 구성'''
url = "http://naver.com"

#조건1: 주어진 url에서 "http://"를 없애라
a = url.replace("http://", "")
print(a)

#조건2: "naver.com"에서 naver만 출력
a = a[:a.index(".")] 
print(a)

#조건3: 남은 글자 중 처음 세자리 + 글자 수 + 글자 내 'e'의 수 + 마지막엔 "!"
password = a[0:3] + str(len(a)) + str(a.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url, password))

