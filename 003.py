python = "python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #python변수의 첫번째 글자가 대문자인가?
print(len(python)) #python변수에 저장된 문자의 길이
print(python.replace("python", "java")) #python이라는 글자를 찾아서 java로 변경후 출력

index = python.index("n") #n이 몇번째에 있는가?
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))