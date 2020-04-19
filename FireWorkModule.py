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
              background=(0, 0, 0),
              length=2):
    """
    -> The def makes a explosion on SenseHat.
    :param point: the point of explosion.
    :param color: color of explosion.
    :param velocity: velocity of explosion.
    :param background: background color of SenseHat.
    :param length: length of explosion
    """
    
    # Check point is class or list
    if type(point) is list:
        point = Axis(center[0], center[1])
    elif point == 'random':
        x = randint(0, 7)
        y = randint(0, 7)
        point = Axis(x, y)
    
    # Update fire pixel
    for c in range(1, length + 1):
        # Fire axis
        f_up = Axis(point.x, point.y - c)     
        f_down = Axis(point.x, point.y + c) 
        f_left = Axis(point.x - c, point.y) 
        f_right = Axis(point.x + c, point.y) 
        
        # Check axis
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
        
        # Update Background
        sleep(velocity)
        sense.clear(background)
        
        
def fire(length = 2,
         color = (200, 200, 200),
         limit = 'random',
         ground = 'random',
         background = (0, 0, 0),
         velocity = 1 / 5):
            
    
    """
    -> The def launch a complete firework on led matrix of SenseHat, calls
    stick and explosion functions to make complete firework.
    :param length: the length of firework.
    :param color: color of firework.
    :param limit: limit of firework.
    :param ground: position in ground where launchs firework.
    :param background: background color of SenseHat.
    :param velocity: velocity of firework.
    """
    
    # Check ground param
    if ground == 'random':
        ground = randint(0, 7)
    
    # Check limit param
    if limit == 'random':
        limit = randint(2, 7)
    
    # Calls stick and explosion def
    point = stick(length,
                  color,
                  limit,
                  ground,
                  background,
                  velocity
                  )
    explosion(point,
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
    
    """
    -> The def stick makes the stick of firework, you can modificate
    the stick with params.
    :param length: the length of stick.
    :param color: color of stick.
    :param limit: limit of stick where he stops.
    :param ground: position in ground where launchs firework.
    :param background: background color of SenseHat.
    :param velocity: velocity of firework.
    """
    
    # Check limit param
    if limit == 'random':
        limit = randint(2, 7)
    
    # Check ground param
    if ground == 'random':
        x = randint(0, 7)
        head = Axis(x, 7)
    else:
        head = Axis(ground, 7)
    
    # Update loop
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

