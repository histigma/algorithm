"""
BJ - Silver 4 - 괄호

"""
from collections import deque

string = input('paranthesis=')

q = deque(string)
r = []

for i, s in enumerate(q, start=1):
    if i == len(q):
        if s == q[0]:
            r.append(1)
        else:
            r.append(-1)
        continue
    if s == q[i+1]:
        r.append(1)
    else:
        r.append(-1)

result = sum(r)
print(result)

#   ( ( ) ) ( ) ( ) 
#   1 2 3 4 5 6 7 8
#   1 0 1 0
