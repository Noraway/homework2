numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    sum_of_sums = 0
    for j in numbers:
        is_prime = True
        if i % j == 0:
            sum_of_sums += 1
    if sum_of_sums != 2:
        is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Prime numbers:', primes)
print('Non-prime numbers:', not_primes)

print()
# По условию задачи not_primes включает в себя ВСЕ НЕ ПРОСТЫЕ ЧИСЛА, поэтому
# окончательный список not_primes включает в себя единицу.
# Если под not_primes понимаются только составные числа, то решение задачи выглядит так:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, len(numbers) + 1):
    sum_of_sums = 0
    for j in range(2, len(numbers) + 1):
        is_prime = True
        if i % j == 0:
            sum_of_sums += 1
    if sum_of_sums > 1:
        is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Prime numbers:', primes)
print('Non-prime numbers:', not_primes)