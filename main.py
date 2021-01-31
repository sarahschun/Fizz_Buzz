
for number in range(1, 101):

    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    # divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # divisible by 5
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)

