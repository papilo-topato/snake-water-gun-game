import random

def user_options(c,u):
    if compran == 1:
        if u == 's':
            print('no loss no win')
        elif u == 'w':
            print('you lose')
        elif u == 'g':
            print('you win!!')
    
    if compran == 2:
        if u == 'w':
            print('no loss no win')
        elif u == 's':
            print('you lose')
        elif u == 'g':
            print('you win!!')

    if compran == 3:
        if u == 'g':
            print('no loss no win')
        elif u == 'w':
            print('you lose')
        elif u == 's':
            print('you win!!')
    return (comp,u)
        

print("comp turn : snake(s) or water(w) or gun(g) : ")
compran = random.randint(1, 3)
if compran == 1:
    comp = 's'
elif compran == 2 :
    comp = 'w'
else :
    comp = 'g'

d = input('your turn : snake(s) or water(w) or gun(g) : ')

print (user_options (comp , d))