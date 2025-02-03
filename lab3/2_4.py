def prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]


numbers = [1, 2, 3, 4, 10, 45, 7, 9, 15, 17, 23]
prime_numbers = filter_prime(numbers)
print(prime_numbers)
