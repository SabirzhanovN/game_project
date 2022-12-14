from random import randint


def send_math():
    return f'{randint(10, 25)} + {randint(10, 25)} = ?'


def check_math(math, ans):
    try:
        ans = int(ans)
    except Exception:
        return False
    else:
        number1 = int(math[:3])
        number2 = int(math[5:7])

        if number1 + number2 == ans:
            return True
        else:
            return False

