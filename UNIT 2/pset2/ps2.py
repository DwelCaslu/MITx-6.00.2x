# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        
        self.width = width
        self.height = height
        self.tile_cleaned = [[False for x in range(width)] for y in range(height)]
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x_pos = math.floor(pos.x)
        y_pos = math.floor(pos.y)
        self.tile_cleaned[y_pos][x_pos] = True
        
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tile_cleaned[n][m]
    
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height
    

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.tile_cleaned[i][j]==True:
                    count+=1
        return count
    

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #(0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).
        #(m, n)
        
        #For debugging:
        #random.seed(0)
       
        m = (self.width-1)*(random.randint(0,1000)/1000)
        n = (self.height-1)*(random.randint(0,1000)/1000)
        
        return Position(m,n)
    

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x_pos = math.floor(pos.x)
        y_pos = math.floor(pos.y)
        
        if x_pos>=0 and x_pos<=self.width-1 and y_pos>=0 and y_pos<=self.height-1:
            return True
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        #Initializes a Robot with the given speed in the specified room:
        self.room=room
        self.speed = speed
        
        #The robot initially has a random direction and a random position
        self.dir = random.randint(0,360)
        self.pos = self.room.getRandomPosition()
        
        #The robot cleans the tile it is on
        self.room.cleanTileAtPosition(self.pos)
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.dir
    

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position
        

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.dir = direction
        

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #self.pos = self.pos 
        #self.room.cleanTileAtPosition(self.pos)
        raise NotImplementedError


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.
    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        old_pos = self.getRobotPosition()
        old_angle = self.getRobotDirection()
        delta_x = self.speed * math.sin(math.radians(old_angle))
        delta_y = self.speed * math.cos(math.radians(old_angle))
        new_x = old_pos.x + delta_x
        new_y = old_pos.y + delta_y
        self.pos = Position(new_x, new_y)
        
        
        while self.room.isPositionInRoom(self.pos) == False: 
            self.dir = random.uniform(0,360)
            delta_x = self.speed * math.sin(math.radians(self.dir))
            delta_y = self.speed * math.cos(math.radians(self.dir))
            new_x = old_pos.x + delta_x
            new_y = old_pos.y + delta_y
            self.pos = Position(new_x, new_y)
 
        self.room.cleanTileAtPosition(self.pos)
        # raise NotImplementedError


# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    clockTicksList = []
    
    for t in range(num_trials):
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height) # 可视化代码
        room = RectangularRoom(width, height)
        robots = []
        for r in range(num_robots):
            robot = robot_type(room, speed)
            robots.append(robot)
            
        # 参数room的引用传递，因此如果都是同一room参数的StandardRobot，那么其中包含的room都指向该room
        # 因此，robots[0]的room即是共同的那个room
        clockTicks = 0
        while room.getNumCleanedTiles() / float(room.getNumTiles()) < min_coverage:
            for robot in robots:
                #anim.update(room, robots) # 可视化代码
                robot.updatePositionAndClean()
            clockTicks += 1
        clockTicksList.append(clockTicks)
        #anim.done() # 可视化代码
    
    return sum(clockTicksList) / float(num_trials)
    # raise NotImplementedError


# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        old_pos = self.getRobotPosition()
        new_angle = random.uniform(0,360) # 第一次update时便需要随机新角度
        delta_x = self.speed * math.sin(math.radians(new_angle))
        delta_y = self.speed * math.cos(math.radians(new_angle))
        new_x = old_pos.x + delta_x
        new_y = old_pos.y + delta_y
        self.pos = Position(new_x, new_y)
        self.dir = random.uniform(0,360)
        
        # 碰撞检查，重选角度，因为可能多次超出room，所以用while； 
        # 第一次初始update不可并入while，因为第一次update前的self.pos一定不超出room
        while self.room.isPositionInRoom(self.pos) == False: 
            self.dir = random.uniform(0,360)
            delta_x = self.speed * math.sin(math.radians(self.dir))
            delta_y = self.speed * math.cos(math.radians(self.dir))
            new_x = old_pos.x + delta_x
            new_y = old_pos.y + delta_y
            self.pos = Position(new_x, new_y)
 
        self.room.cleanTileAtPosition(self.pos)
        
        # raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room', 'Number of Robots ', 'Time-steps')
 
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

showPlot2('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms', 'Aspect Ratio', 'Time-steps')

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
