

arr= list(map(int, input('arr>').split()))

min = arr[0]
max = arr[0]
for i in arr[1:]:
    if i > max:
        max = i
    if i < min:
        min = i

print(min, max)



