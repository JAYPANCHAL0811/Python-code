def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        # range(2, 7)
        # i = 2, 3, 4, 5, 6

        if num % i == 0:
            # Check if 7 is divisible by i

            # i = 2
            # 7 % 2 = 1
            # is it: 1 == 0  False

            # i = 3
            # 7 % 3 = 1
            # is it: 1 == 0  False

            # i = 4
            # 7 % 4 = 3
            # is it: 3 == 0  False

            # i = 5
            # 7 % 5 = 2
            # is it: 2 == 0  False

            # i = 6
            # 7 % 6 = 1
            # is it: 1 == 0  False

            return False

    return True


num = 7

if is_prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")