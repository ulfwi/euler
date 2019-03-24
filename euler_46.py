import math

def increase_prime_list(prime_list):
    new_prime = prime_list[-1]

    prime_found = False
    while not prime_found:
        new_prime += 2
        sqrt_prime = int(math.sqrt(new_prime))
        for prime in prime_list:
            if prime <= sqrt_prime:
                if new_prime % prime == 0:
                    # new_prime is not a prime number
                    break
                elif prime == sqrt_prime:
                    prime_list += [new_prime]
                    prime_found = True
                    break
            else:
                prime_list += [new_prime]
                prime_found = True
                break

prime_list = [2, 3]

number = 9
while True:

    while prime_list[-1] < number:
        increase_prime_list(prime_list)

    for prime in prime_list:
        base = 1
        while prime + 2*base**2 != number and prime + 2*base**2 <= number:
            base += 1

        if prime + 2*base**2 == number:
            print(str(number) + " = " + str(prime) + " + 2*" + str(base) + "^2")
            break
    
    if prime + 2*base**2 != number:
        print("Not found! " + str(number))
        break

    # increment number
    number += 2
    while number in prime_list:
        number += 2
