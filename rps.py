import random
print('rps')

while True:
    inp=input('rock paper or scissor: ')
    n=random.randint(1,3)
    inp=inp.lower
    try:
        if inp=='rock':
            if n==1:
                print('draw')
            if


    except Exception as ex:
        print('enter a valid answer')