import random
print('rps')
print('to quit type quit')
while True:
    inp=input('rock paper or scissor: ')
    n=random.randint(1,3)
    inp=inp.lower()
    if inp=='rock':
        if n==1:
                print('draw')
        if n==2:
            print('you lose')
        if n==3:
            print('you win')
        print('now we start again')
    elif inp=='paper':
        if n==1:
            print('you win')
        if n==2:
            print('draw')

        if n==3:
            print('you lose')
        print('now we start again')
    elif inp=='scissor':
        if n==1:
            print('you lose')
        if n==2:
            print('you win')

        if n==3:
            print('draw')
        print('now we start again')
    elif inp=='quit':
        break
    else:
        print('enter a valid answer')
print('you quit the game')