"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("Value should be more than 0")

    else:
        num = 2
        counter = 0

        while ctr < number_of_primes:
            is_Prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_Prime = False

            if is_Prime:
                list.append(num)
                counter +=1
            
            num = num + 1
    return list
