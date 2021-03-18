#리스트(배열) []

#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
# 위가 기존의 방식 이었다면 이젠 하나의 리스트에 넣기
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#유재석은 몇번째 칸에 있는가?
print(subway.index("유재석"))

#하하 추가
subway.append("하하")
print(subway)

#유재석과 조세호 사이에 정형돈 추가
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람 뒤에서 한명 씩 내림
print(subway.pop(2))
print(subway)

#같은 이름의 사람이 몇 명 있는 지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
num = [5,2,4,3,1]
num.sort()
print(num)

# 순서 반대로
num.reverse()
print(num)

# 모두 지우기
num.clear()
print(num)

# 다양한 자료형 함께 사용
list = ["치킨", 2, True]
print(list)

# 리스트 합치기
num = [5,2,4,3,1]
num.extend(list)
print(num)