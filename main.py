from p5 import *
import numpy as np
from boids import Boid

width = 500
height = 500
flock = [Boid(*np.random.rand(2)*width,width,height) for _ in range(50)]
def setup():
    #this happens just once
    size(width, height) #instead of create_canvas



def draw():
    #this happens every time
    background(30, 30, 47)
    for boid in flock:
        boid.show()
        boid.apply_behaviour(flock)
        boid.update()
run()