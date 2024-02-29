
def is_prime(num):
    if num < 1: # special case, early exit
        return False

    for i in range(2, int(num / 2) + 1): # If num is divisible by any number between
        if (num % i) == 0:
            print(f'{num} is NOT a prime number, returning False')
            return False

    print(f'{num} is a prime number, returning True')
    return True


for j in range(51):
    is_prime(j)


