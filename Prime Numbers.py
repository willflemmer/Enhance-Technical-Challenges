#find prime numbers up to X
#add prime numbers to list
#check if X is in prime number list

def prime_checker(number):
    primes = [2]

    for num in range(2, number + 1):
        count = 0
        for prime in primes:
            if num % prime == 0:
                count += 1
            if count != 0:
                break

        if count == 0:
            primes.append(num)

    if number in primes:
        return True
    else:
        return False

result = prime_checker(6)
print(result)