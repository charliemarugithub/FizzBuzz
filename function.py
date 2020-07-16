def fizz_buzz(input):
    # checking number with modulus 3 and 5 first
    # if input % 3 == 0 was first, we would always get Fizz
    # as the answer if input was 0
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(25))
