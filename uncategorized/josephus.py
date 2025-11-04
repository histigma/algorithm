"""
BJ - Silver 4 - 요세푸스 문제

https://github.com/VSFe/Algorithm_Study/blob/main/Concept/Prev/vol.1/01_Queue_Stack/Ch.01_%ED%81%90_%EC%8A%A4%ED%83%9D_Python.pdf

"""

from collections import deque

n = int(input('n='))
k = int(input('k='))

if not (1 <= k <= n <= 1000):
    raise ValueError(
        "Abnormal range"
    )

result = []
circle = deque(range(1, n + 1))

i = 0
while len(circle) > 0:
    i += 1
    if i % k == 0:
        r = circle.popleft()
        result.append(r)
    else:
        circle.append(
            circle.popleft()
        )

print(result)

