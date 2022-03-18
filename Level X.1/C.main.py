import random

numbers = []
primeNumbers = [2, 3, 5, 7, 11]

for i in range(10):
    chosenNumbers = random.randint(0, 999)
    numbers.append(chosenNumbers)
print("these are the original numbers chosen: {}".format(numbers))
print("")

for a in primeNumbers:
    print("if these numbers above are divisible by {} then it will appear below.".format(a))
    divisibleByPrimes = []
    for n in numbers:
        if n % a == 0:
            divisibleByPrimes.append(n)

    print("")

    if divisibleByPrimes != []:
        print(divisibleByPrimes)
        print("")