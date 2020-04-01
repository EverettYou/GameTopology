import numpy as np
import random
class simulator: 
    
    # This starts everyhing at 0
    def __init__(self, size, topology):
        self.food = np.array([0,0])
        self.snake = np.array([0,0])
        self.score = 0
        self.size = size
        self.topology = topology
    
    # Randomizes 
    def start(self):
        self.snake = np.array([random.randint(0,self.size-1),random.randint(0,self.size-1)])
        self.food = np.array([random.randint(0,self.size-1),random.randint(0,self.size-1)])
        
            
    def act(self, action):
        
        # moves left 
        if action == 'left':
            self.snake += np.array([-1,0])
        
        # moves right
        if action == 'right':
            self.snake += np.array([1,0])
            
        # moves up 
        if action == 'up':
            self.snake += np.array([0,1])
        
        # moves down
        if action == 'down':
            self.snake += np.array([0,-1])
           
                    
        # I want to define the length and width as the size minus one 
        
        height = self.size - 1 
        width = self.size - 1
        
        # Now I will check the boundaries and move the snake accordingly
        if self.topology == 'torus':
            if self.snake[0] < 0:
                self.snake[0] = width
            if self.snake[0] > width:
                self.snake[0] = 0
            if self.snake[1] > height:
                self.snake[1] = 0
            if self.snake[1] < 0:
                self.snake[1] = height
        
        if self.topology == 'sphere':
            if self.snake[0] < 0:
                self.snake[0] = width - self.snake[1]
                self.snake[1] = width
            if self.snake[0] > width: 
                self.snake[0] = height - self.snake[1]
                self.snake[1] = 0 
            if self.snake[1] > height:
                
                self.snake[1] = height - self.snake[0]
                self.snake[0] = 0
            if self.snake[1] < 0: 
                
                self.snake[1] = height - self.snake[0]
                self.snake[0] = height
        
        if self.topology == '2-torus':
            
            # Half of the height
            halfHeight = (1/2)*height
            # Half of the length
            halfWidth = (1/2)*width
            if self.snake[0] < 0:
                if self.snake[1] <= (1/2)*height:
                    self.snake[0] = (1/2)*width - self.snake[1] 
                    self.snake[1] = height
                if self.snake[1] > (1/2)*height:
                    self.snake[0] = (3/2)*width - self.snake[1]
                    self.snake[1] = height
            if self.snake[0] > width:
                if self.snake[1] <= (1/2)*height:
                    self.snake[0] = (1/2)*width - self.snake[1]
                    self.snake[1] = 0
                if self.snake[1] > (1/2)*height:
                    self.snake[0] = (3/2)*width - self.snake[1] 
                    self.snake[1] = 0 
            if self.snake[1] > height:
                if self.snake[0] <= (1/2)*width:
                    self.snake[1] = (1/2)*width - self.snake[0]
                    self.snake[0] = 0
                if self.snake[0] > (1/2)*width:
                    self.snake[1] = (3/2)*width - self.snake[0]
                    self.snake[0] = 0
            if self.snake[1] < 0:
                if self.snake[0] <= (1/2)*width:
                    self.snake[1] = (1/2)*width - self.snake[0]
                    self.snake[0] = 0
                if self.snake[0] > (1/2)*width:
                    self.snake[1] = (3/2)*width - self.snake[0]
                    self.snake[0] = 0
            
            
        #checking if snake touched food    
        if (self.food==self.snake).all():
                self.score = self.score + 1
                self.food = np.array([random.randint(0,height),random.randint(0,height)])
        
        # Make sure that snake has a tail that extends, perhaps through a recursive function?
                
        
    def board(self):
        
        bd = np.zeros((self.size,self.size))
        bd[self.snake[0],self.snake[1]] = -1
        bd[self.food[0],self.food[1]] = 1
        
        # put a +1 at food position
        #-1 at snake
        return bd
        