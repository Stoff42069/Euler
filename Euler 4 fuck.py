def is_palindrome(num):
    return str(num) == str(num)[::-1]
def largest(bot, top):
    z = 0
    for x in range(top, bot, -1):
        for y in range(top, bot, -1):
            if is_palindrome(x * y):
                if x * y > z:
                    z = x * y
    return z
print(largest(100,999))