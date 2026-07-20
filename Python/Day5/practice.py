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
-------------------------------------------------------------
for i in range(10, 1, -3):
...  print(i)
...
10
7
4
-------------------------------------------------------------
#짝수 출력 
for i in range(2,10,2):
...  print(i)
...
2
4
6
8
-------------------------------------------------------------
count = 0
>>> while True:
...  if count > 3:
...     break
...  print(count)
...  count += 1
...
0
1
2
3
#while문에 True가 있어 무한 반복이였으나 break를 통해  탈출을 시켜 주었다
-------------------------------------------------------------
#i가 짝수라면 print를 실행하지 않고 바로 continue를 통해 다음 수로 넘어가는 코드
>>> for i in range(5):
...  print(i)
...  if i % 2 ==0:
...     continue
...  print("===")
...
0
1
===
2
3
===
4
