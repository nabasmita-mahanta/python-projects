def is_prime(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def print_prime(num):
    if num == 1:
        pass
    elif num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                break
        else:
            print(num)
    else:
        pass
