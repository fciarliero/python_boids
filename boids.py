from p5 import *

class Boid():

    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.position = Vector(x, y)
        #A vector is an entity that has both magnitude and direction
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)
        self.vel_max = 5
        vec = (np.random.rand(2) - 0.5)/2
        self.perception = 200

        self.acceleration = Vector(*vec) 
    def show(self):
        stroke(255)
        #triangle((self.position.x,self.position.y - 4),(self.position.x + 2, self.position.y + 4),(self.position.x - 2,self.position.y + 4))
        circle((self.position.x, self.position.y),5)
        
    def keep_in_bounds(self):
        if self.position[0] > self.width or self.position[0] <= 0:
            self.velocity[0] = -self.velocity[0]
            self.acceleration[0] = -self.acceleration[0]
        if self.position[1] > self.height or self.position[1] <= 0:
            self.velocity[1] = -self.velocity[1]
            self.acceleration[1] = -self.acceleration[1]
            
    def normalize_acceleration(self):
        if np.linalg.norm(self.velocity) > self.vel_max:
            self.velocity = (self.velocity / np.linalg.norm(self.velocity)) * self.vel_max
            self.acceleration = Vector(0,0)
            
    def align(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vec = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception:
                avg_vec += boid.velocity
                total += 1
        if total > 0:
            avg_vec /= total
            avg_vec = Vector(*avg_vec)
            avg_vec = (avg_vec /np.linalg.norm(avg_vec)) * self.vel_max
            steering = avg_vec - self.velocity

        return steering
        
    def apply_behaviour(self, boids):
        alignment = self.align(boids)
        self.acceleration += alignment
        
    def infinite_world(self):
        self.position[0] = self.position[0] % self.width
        self.position[1] = self.position[1] % self.height

    def update(self):
        #self.keep_in_bounds()
        self.infinite_world()
        self.normalize_acceleration()
        self.position += self.velocity
        self.velocity += self.acceleration
        