# Simple is_prime time: O(sqrt(n))
def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            return False
        i += 1
    return True

# Simple search next prime time: O(n)
def next_prime(num):
    if num < 0:
        raise Exception("Illegal input! num cannot be negative")
    curr = num + 1
    
    while not is_prime(curr):
        curr += 1
    return curr

# Brute force search factors time: O(n)
def search_prime_factors(number):
    if is_prime(number):
        return [number]
    
    factors = []
    
    num = number
    curr = 2
    while num > 1:
        if curr > number:
            raise Exception("How?")
        
        if num % curr == 0:
            factors.append(curr)
            num /= curr
            curr = 2
        else:
            curr = next_prime(curr)
    return factors

print("Finding 1003 prime factors")
print(search_prime_factors(1003))