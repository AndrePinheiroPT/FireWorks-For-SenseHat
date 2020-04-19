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
    
    
def explosion(point='random',
              color=(200, 200, 200),
              velocity=1/5,
              background=(0, 0, 0)
              ):
    """
    -> The def makes a explosion of firework after launch
    :param center: the head of firework
    :param color_ex: color of explosion
    :param time: explosion time
    :param background_ex: background color of SenseHat
    """

    if type(point) is list:
        point = Axis(center[0], center[1])
    elif point == 'random':
        x = randint(0, 7)
        y = randint(0, 7)
        head = Axis(x, y)

    for c in range(1, 3):
        f_up = Axis(point.x, point.y - c)     
        f_down = Axis(point.x, point.y + c) 
        f_left = Axis(point.x - c, point.y) 
        f_right = Axis(point.x + c, point.y) 
        
        if f_up.y >= 0:
            sense.set_pixel(
                f_up.x,
                f_up.y,
                color
            )
        if f_down.y <= 7:
            sense.set_pixel(
                f_down.x,
                f_down.y,
                color
            )
        if f_left.x >= 0:
            sense.set_pixel(
                f_left.x,
                f_left.y,
                color
            )
        if f_right.x <= 7:
            sense.set_pixel(
                f_right.x,
                f_right.y,
                color
            )
        
        sleep(velocity)
        sense.clear(background)
        
        
def fire(color = (200, 200, 200),
         ground = 'random',
         velocity = 1 / 5,
         background = (0, 0, 0),
         limit = 'random',
         length = 2):
    
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
    
    if ground == 'random':
        ground = randint(0, 7)
    
    if color == 'random':
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        
    if limit == 'random':
        limit = randint(2, 7)
    
    center = stick(length,
                  color,
                  limit,
                  ground,
                  background,
                  velocity
                  )
    explosion(center,
              color,
              velocity,
              background
              )
    
    
def stick(length = 2,
          color = (200, 200, 200),
          limit = 'random',
          ground = 'random',
          background = (0, 0, 0),
          velocity = 1 / 5):
    
    if limit == 'random':
        limit = randint(2, 7)
        
    if ground == 'random':
        x = randint(0, 7)
        head = Axis(x, 7)
    else:
        head = Axis(ground, 7)
        
    for update in range(0, limit):
        # Change x axis every update
        tail = []
        for y in range(head.y + 1, head.y + length):
            tail.append(y)
            
        # Show head of fire
        sense.set_pixel(head.x, head.y, color)
        for part in tail:
            try:
                sense.set_pixel(head.x, part, color)
            except:
                print('> Show no stick')
            
        # Update every pixel    
        head.y -= 1
        
        # Change background every update
        sleep(velocity)
        sense.clear(background)
    
    # return head state
    return head


