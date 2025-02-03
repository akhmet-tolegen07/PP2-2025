def prime(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 3, 5, 8, 13, 17, 20, 23, 29, 35]

prime_numbers = list(filter(lambda x: prime(x), numbers))

print(prime_numbers)
