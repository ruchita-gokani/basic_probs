"""Find out the prime numbers in 1 to 100"""


def is_prime(num1):
    fact = {}
    prime_num = []
    for i in range(1, num1+1):
        for j in range(1, i+1):
            if i%j == 0:
                if i in fact:
                    fact[i].append(j)
                else:
                    fact[i] = [j]
        if len(fact[i]) <= 2:
            prime_num.append(i)

    return prime_num


if __name__ == '__main__':
    num1 = 100
    print(is_prime(num1))
