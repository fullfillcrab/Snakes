import curses
from random import randint

#Setup window
curses.initscr()
win=curses.newwin(20, 60, 0, 0) #y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Snake And Food
Snake=[(4,10), (4,9), (4,8)]
food=(10,20)

win.addch(food[0],food[1],'#')
#Game Logic
score=0

ESC = 27
key=curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(Snake)) // 5 + len(Snake)//10 % 120) #increase speed as per length

    prev_key=key
    event = win.getch()
    key=event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key=prev_key

    #calculate next coordinates of snake
    y=Snake[0][0]
    x=Snake[0][1]
    if key==curses.KEY_DOWN:
        y+=1
    if key==curses.KEY_UP:
        y-=1
    if key==curses.KEY_RIGHT:
        x+=1
    if key==curses.KEY_LEFT:
        x-=1
    Snake.insert(0, (y,x))

    #Check for hit with border
    if y==0: break
    if y==19: break
    if x==0: break
    if x==59: break 
    
    #Check for hit with snake
    if Snake[0] in Snake[1:]: break

    if Snake[0]==food:
        #eat the food
        score+=1
        food=()
        while food==():
            food=(randint(1, 18), randint(1, 58))
            if food in Snake:
                food=()
        win.addch(food[0],food[1],'#')
    else:
        #move snake
        last = Snake.pop()
        win.addch(last[0],last[1],' ')

    win.addch(Snake[0][0],Snake[0][1],'*')

curses.endwin()
print(f"Final Score = {score}")