#리스트

#지하철 칸별로 10명, 20명, 30명
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
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는 지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
num = [5,2,4,3,1]
num.sort()
print(num)