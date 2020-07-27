


def fizz_buzz():
    for num in range(1, 101):
        # really good for readability and code maintenance - where'd you pick that up
        fizzing = num % 3 == 0
        buzzing = num % 5 == 0
        # slight clean up for less equality checks
        if fizzing and buzzing:
            print('FizzBuzz')
        elif fizzing:
            print('Fizz')
        elif buzzing:
            print('Buzz')
        else:
            print(num)

fizz_buzz()
