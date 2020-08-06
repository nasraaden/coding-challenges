'''
Check if all digits of the given integer are even.
'''


def evenDigitsOnly(n):
    n = list(str(n))
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            return False
    return True


n = 248622

print(evenDigitsOnly(n))
