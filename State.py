import random
import copy
from queue import PriorityQueue

class Const:
    UNIT_SIZE = 10

class Vector:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def show(self):
        print("[", self.X, ", ", self.Y, "]")
    
    def Update(self, X, Y):
        self.X = X
        self.Y = Y
        
    def Add(self, Vec):
        self.X = self.X + Vec.X
        self.Y = self.Y + Vec.Y

class Maze:
    def __init__(self, PuzzleFileName):
        self.MAP = []
        self.LoadMaze(PuzzleFileName)
    
    def LoadMaze(self, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            [self.HEIGHT, self.WIDTH] = [int(digit) for digit in line.split()]
            self.MAP = [[int(digit) for digit in line.split()] for line in f]

class Snake:
    def __init__(self, Color, HeadPositionX=10, HeadPositionY=10, HeadDirectionX=1, HeadDirectionY=0):
        self.Size = 1
        self.Body = [] #in this implementation the body is empty
        self.Color = Color
        self.HeadPosition = Vector(HeadPositionX, HeadPositionY)
        self.HeadDirection = Vector(HeadDirectionX, HeadDirectionY)
        self.score = 0
        self.isAlive = True
    
    def moveSnake(self, State):
        if not self.isAlive:
            return

        self.HeadPosition.Add(self.HeadDirection)

        r = self.HeadPosition.Y
        c = self.HeadPosition.X
        
        if (r >= State.maze.HEIGHT or r < 0) or (c >= State.maze.WIDTH or c < 0):
            self.isAlive = False
        elif State.maze.MAP[r][c] == -1:
            self.isAlive = False
        elif c == State.FoodPosition.X and r == State.FoodPosition.Y:
            self.score = self.score + 10

class SnakeState:
    def __init__(self, Color, HeadPositionX, HeadPositionY, HeadDirectionX, HeadDirectionY, mazeFileName):
        self.snake = Snake(Color, HeadPositionX, HeadPositionY, HeadDirectionX, HeadDirectionY)
        self.maze = Maze(mazeFileName)
        self.generateFood()

      
    def __lt__(self, other):
        return id(self) < id(other)

    def generateFood(self):
        """
        Method to randomly place a circular 'food' object anywhere on Canvas.
        The tag on it is used for making decisions in the program
        """
        FoodFlag = False
        while not FoodFlag:
            x = random.randrange(3, self.maze.WIDTH  - 3)
            y = random.randrange(3, self.maze.HEIGHT - 3)

            if self.maze.MAP[y][x] != -1:
                FoodFlag = True
                
        self.FoodPosition = Vector(x, y)