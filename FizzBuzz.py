
def fizz_buzz():
    for num in range(1, 101):
        fizzing = num % 3 == 0
        buzzing = num % 5 == 0
        if fizzing and not buzzing:
            print('Fizz')
        elif num % 5 == 0 and not fizzing:
            print('Buzz')
        elif fizzing and buzzing:
            print('FizzBuzz')
        else:
            print(num)

fizz_buzz()