from time import sleep
from random import randint
from sense_hat import SenseHat

sense = SenseHat()

#############
# FIREWORKS #
#############
# Created by: André Pinheiro

class Axis:
    """
    The class creat x and y axis of
    object
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def explosion(center, color_ex, time, background_ex):
    """
    -> The def makes a explosion of firework after launch
    :param center: the head of firework
    :param color_ex: color of explosion
    :param time: explosion time
    :param background_ex: background color of SenseHat
    """
    for c in range(1, 3):
        f_up = Axis(center.x, center.y - c)     
        f_down = Axis(center.x, center.y + c) 
        f_left = Axis(center.x - c, center.y) 
        f_right = Axis(center.x + c, center.y) 
        
        if f_up.y >= 0:
            sense.set_pixel(
                f_up.x,
                f_up.y,
                color_ex
            )
        if f_down.y <= 7:
            sense.set_pixel(
                f_down.x,
                f_down.y,
                color_ex
            )
        if f_left.x >= 0:
            sense.set_pixel(
                f_left.x,
                f_left.y,
                color_ex
            )
        if f_right.x <= 7:
            sense.set_pixel(
                f_right.x,
                f_right.y,
                color_ex
            )
        
        sleep(time)
        sense.clear(background_ex)
        
        
def fire(color_p=(200, 200, 200),
         position='random',
         velocity=1/3,
         background=(0, 0, 0),
         height=randint(1, 7)):
    
    """
    -> The def launch firework in SenseHat, set
    the head a stick axis, update pixels and calls
    the explosion def
    :param color_p: color of firework, you can select the color or
    a random color
    :param position: position of pixel launchs firework,
    you can set the pixel or a random pixel
    :param velocity: velocity of firework
    :param background: background color of SenseHat
    :param height: height of firework
    """
    
    if position == 'random':
        x = randint(0, 7)
    else:
        x = position
    
    if color_p == 'random':
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
    else:
        color = color_p
    
    # Set head and corp of firework
    head = Axis(x, 7)
    stick = Axis(x, head.y + 1)
        
    for update in range(0, height):
        # Show head of fire
        sense.set_pixel(head.x, head.y, color)
        
        try:
            sense.set_pixel(stick.x, stick.y, color)
        except:
            print('> Show no stick')
            
        # Up and update every pixel    
        head.y -= 1
        stick.y -= 1
        
        sleep(velocity)
        sense.clear(background)
        
    explosion(head, color, velocity, background)

