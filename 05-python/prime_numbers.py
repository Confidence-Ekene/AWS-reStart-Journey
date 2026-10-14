# Prime Numbers Generator
# Description: Find prime numbers between 1 and 250
# Save results to results.txt

primes = []

for number in range(2, 251):
    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)

with open("results.txt", "w") as file:
    for prime in primes:
        file.write(str(prime) + "\n")

print("Prime numbers saved to results.txt")
print("Total prime numbers:", len(primes))
