import random
import time
import math
import logging

# Setting up logging for debugging
logging.basicConfig(filename="robot_simulation.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GRID_SIZE = 10  # 10x10 grid environment
ROBOT_MAX_BATTERY = 100  # Max battery level
ROBOT_SPEED = 1  # Steps per move
OBSTACLE = -1
EMPTY = 0
DATA_POINT = 1

# Environment setup (10x10 grid)
environment = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Placing random obstacles and data points
def setup_environment(env):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < 0.2:  # 20% chance of an obstacle
                env[i][j] = OBSTACLE
            elif random.random() < 0.1:  # 10% chance of data point
                env[i][j] = DATA_POINT

setup_environment(environment)

# Robot Class
class Robot:
    def __init__(self, x, y):
        self.x = x  # Robot's position in the environment
        self.y = y
        self.battery = ROBOT_MAX_BATTERY  # Battery level
        self.data_collected = 0  # Number of data points collected
        self.path = []  # Log of robot's movement
        self.environment = environment  # Robot's reference to the environment grid

    def move_forward(self):
        if self.y + 1 < GRID_SIZE and self.environment[self.x][self.y + 1] != OBSTACLE:
            self.y += 1
            self._consume_battery()
            logging.info(f"Moved forward to ({self.x}, {self.y})")

    def move_backward(self):
        if self.y - 1 >= 0 and self.environment[self.x][self.y - 1] != OBSTACLE:
            self.y -= 1
            self._consume_battery()
            logging.info(f"Moved backward to ({self.x}, {self.y})")

    def move_left(self):
        if self.x - 1 >= 0 and self.environment[self.x - 1][self.y] != OBSTACLE:
            self.x -= 1
            self._consume_battery()
            logging.info(f"Moved left to ({self.x}, {self.y})")

    def move_right(self):
        if self.x + 1 < GRID_SIZE and self.environment[self.x + 1][self.y] != OBSTACLE:
            self.x += 1
            self._consume_battery()
            logging.info(f"Moved right to ({self.x}, {self.y})")

    def _consume_battery(self):
        self.battery -= 1
        logging.info(f"Battery level: {self.battery}")
        if self.battery == 0:
            logging.warning("Battery exhausted! Shutting down.")
            print("Battery exhausted! Robot shutting down.")
            exit()

    def scan_for_data(self):
        """Simulate a sensor scan to collect data points around."""
        for i in range(max(0, self.x - 1), min(GRID_SIZE, self.x + 2)):
            for j in range(max(0, self.y - 1), min(GRID_SIZE, self.y + 2)):
                if self.environment[i][j] == DATA_POINT:
                    self.collect_data(i, j)

    def collect_data(self, x, y):
        """Collect data from a particular cell."""
        if self.environment[x][y] == DATA_POINT:
            self.data_collected += 1
            self.environment[x][y] = EMPTY  # Data point collected
            logging.info(f"Collected data at ({x}, {y}). Total data: {self.data_collected}")

    def make_decision(self):
        """Make a decision about where to move based on surroundings."""
        directions = ['forward', 'backward', 'left', 'right']
        random.shuffle(directions)

        for direction in directions:
            if direction == 'forward' and self.y + 1 < GRID_SIZE and self.environment[self.x][self.y + 1] != OBSTACLE:
                self.move_forward()
                return
            elif direction == 'backward' and self.y - 1 >= 0 and self.environment[self.x][self.y - 1] != OBSTACLE:
                self.move_backward()
                return
            elif direction == 'left' and self.x - 1 >= 0 and self.environment[self.x - 1][self.y] != OBSTACLE:
                self.move_left()
                return
            elif direction == 'right' and self.x + 1 < GRID_SIZE and self.environment[self.x + 1][self.y] != OBSTACLE:
                self.move_right()
                return
        logging.info("No valid move found.")

    def display_status(self):
        print(f"Position: ({self.x}, {self.y}), Battery: {self.battery}, Data collected: {self.data_collected}")
        logging.info(f"Status -> Position: ({self.x}, {self.y}), Battery: {self.battery}, Data: {self.data_collected}")

# Simulated Environment Class
class Environment:
    def __init__(self, size):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.obstacles = []
        self.data_points = []

    def setup_obstacles(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < 0.15:
                    self.grid[i][j] = OBSTACLE
                    self.obstacles.append((i, j))

    def place_data_points(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != OBSTACLE and random.random() < 0.1:
                    self.grid[i][j] = DATA_POINT
                    self.data_points.append((i, j))

    def display(self):
        print("Environment Grid:")
        for row in self.grid:
            print(' '.join([str(cell) for cell in row]))

# Simulation Control Class
class Simulation:
    def __init__(self, robot, environment):
        self.robot = robot
        self.environment = environment
        self.running = True

    def run(self):
        steps = 0
        while self.running and steps < 1000:
            steps += 1
            print(f"\nStep {steps}:")
            self.robot.display_status()
            self.robot.scan_for_data()
            self.robot.make_decision()
            self._check_battery()
            time.sleep(0.5)  # Simulate time passing between steps

    def _check_battery(self):
        if self.robot.battery <= 0:
            self.running = False
            print("Simulation Ended: Battery exhausted.")

# Setting up and running the simulation
if __name__ == "__main__":
    # Initialize environment and robot
    environment = Environment(GRID_SIZE)
    environment.setup_obstacles()
    environment.place_data_points()
    environment.display()

    # Start robot at the center of the grid
    robot = Robot(GRID_SIZE // 2, GRID_SIZE // 2)
    
    # Start simulation
    simulation = Simulation(robot, environment)
    simulation.run()
