import mouse
import time
from random import random as gen
from math import sqrt
def sqr(x):
    return x*x


def main():
    
    t = time.time()
    delay_time = gen()*200
    pos = mouse.get_position()
    main_control(t, delay_time, pos)


def main_control(x,y,pos):

#important variable settings.
    t = x
    delay_time = y
    sleep_time = gen()*50
    centre = pos
    
#calls to some mouse logic functions.  loop of main program.

    while True:
        click()
        movement(centre)
            
    #this is the random delay logic.  let program hibernate every
    # time time.time() exceeds t + delay_time.

        if t + delay_time < time.time():
            time.sleep(sleep_time) 
            t = time.time()
            delay_time = gen()*200
                
        else:
            continue


def movement(centre):
#logic for mouse-movement.  centre at initial location of mouse, and then
    #restrict movement to the disk with radius = 8 pixels centred at centre.

    maximum_dist = 8
    origin_x = centre[0]
    origin_y = centre[1]

    new_x = origin_x + gen()*10
    new_y = origin_y + gen()*10
    distance = sqrt(sqr(new_x - origin_x)  + sqr(new_y - origin_y))

    if distance < maximum_dist:
        mouse.move(new_x, new_y, absolute=True, duration = gen()*5)
        

    

def click():
#click randomization logic

    delay_chance = gen()
    click_chance = gen()
    
    if delay_chance > 0.1:
        time.sleep(delay_chance)
    else:
        time.sleep(delay_chance + gen())
        
    if click_chance > 0.5:
        mouse.click(button='left')

if __name__ == '__main__':
    main()
