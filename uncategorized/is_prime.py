
num = int(input('num='))

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print('소수 여부:', is_prime(num))
