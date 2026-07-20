</> python

bool(0.0)
False  #0.0 부울값이 0이라는 것을 확인

 a = 0
>>> if a:  #a가 0이므로 False이다 따라서 else식을 실행
...     print("a is not Zero")
... else:
...     print("a is Zero")
...
a is Zero
-------------------------------------------------------------
total = 0
index = 0
while index < len(subject):
...  total += subject[index]
...  index += 1
... total/4
...
88.5
-------------------------------------------------------------
for letter in "안녕하세요":
...  print(letter)
...
안
녕
하
세
요
-------------------------------------------------------------
 total = 0
>>> subject = [90,88,91,94,92]
>>> for score in subject:
...  total += score
...
>>> total / len(subject)
91.0
