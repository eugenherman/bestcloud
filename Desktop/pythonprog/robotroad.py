import random
import time
import logging

# Set up logging to track robot actions
logging.basicConfig(filename="robot_road.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
ROAD_LENGTH = 20  # Length of the road grid
ROAD_WIDTH = 5  # Number of lanes on the road
TRAFFIC_SIGNAL_INTERVAL = 5  # Every 5 units, there's a traffic light
ROBOT_MAX_BATTERY = 100  # Max battery level
OBSTACLE = -1
EMPTY = 0
TRAFFIC_LIGHT_RED = 'R'
TRAFFIC_LIGHT_GREEN = 'G'

# The road grid
road = [[EMPTY for _ in range(ROAD_LENGTH)] for _ in range(ROAD_WIDTH)]

# Place random obstacles (other cars or roadblocks)
def setup_obstacles(road):
    for i in range(ROAD_WIDTH):
        for j in range(ROAD_LENGTH):
            if random.random() < 0.1:  # 10% chance of an obstacle
                road[i][j] = OBSTACLE

setup_obstacles(road)

# Traffic Light System
class TrafficLight:
    def __init__(self, interval):
        self.interval = interval
        self.position = [i for i in range(0, ROAD_LENGTH, interval)]
        self.state = {pos: random.choice([TRAFFIC_LIGHT_GREEN, TRAFFIC_LIGHT_RED]) for pos in self.position}

    def update_lights(self):
        for pos in self.position:
            if self.state[pos] == TRAFFIC_LIGHT_RED:
                self.state[pos] = TRAFFIC_LIGHT_GREEN
            else:
                self.state[pos] = TRAFFIC_LIGHT_RED

    def get_light_state(self, x_pos):
        """Return the traffic light state at the current x-position."""
        return self.state.get(x_pos, None)

# Robot Class
class Robot:
    def __init__(self, lane, position, battery=ROBOT_MAX_BATTERY):
        self.lane = lane  # Robot's lane (row in the road grid)
        self.position = position  # Robot's position along the road (column in the grid)
        self.battery = battery  # Battery level
        self.speed = 1  # Movement speed (1 unit per move)
        self.traffic_light = TrafficLight(TRAFFIC_SIGNAL_INTERVAL)
        self.obstacle_detected = False

    def move_forward(self):
        if self.position + 1 < ROAD_LENGTH:
            if road[self.lane][self.position + 1] == OBSTACLE:
                self.obstacle_detected = True
                logging.warning("Obstacle detected! Stopping robot.")
            elif self.traffic_light.get_light_state(self.position + 1) == TRAFFIC_LIGHT_RED:
                logging.info("Stopped at red traffic light.")
            else:
                self.position += self.speed
                self._consume_battery()
                logging.info(f"Moved forward to position ({self.lane}, {self.position})")

    def move_backward(self):
        if self.position - 1 >= 0:
            if road[self.lane][self.position - 1] == OBSTACLE:
                self.obstacle_detected = True
                logging.warning("Obstacle detected behind! Stopping robot.")
            else:
                self.position -= self.speed
                self._consume_battery()
                logging.info(f"Moved backward to position ({self.lane}, {self.position})")

    def move_left(self):
        if self.lane - 1 >= 0:
            if road[self.lane - 1][self.position] == OBSTACLE:
                self.obstacle_detected = True
                logging.warning("Obstacle detected on the left! Can't move left.")
            else:
                self.lane -= 1
                self._consume_battery()
                logging.info(f"Moved left to lane {self.lane}")

    def move_right(self):
        if self.lane + 1 < ROAD_WIDTH:
            if road[self.lane + 1][self.position] == OBSTACLE:
                self.obstacle_detected = True
                logging.warning("Obstacle detected on the right! Can't move right.")
            else:
                self.lane += 1
                self._consume_battery()
                logging.info(f"Moved right to lane {self.lane}")

    def _consume_battery(self):
        self.battery -= 1
        if self.battery <= 0:
            logging.error("Battery exhausted! Shutting down.")
            print("Battery exhausted! Robot shutting down.")
            exit()
        logging.info(f"Battery level: {self.battery}")

    def scan_obstacle(self):
        """Scan ahead for obstacles."""
        if self.position + 1 < ROAD_LENGTH and road[self.lane][self.position + 1] == OBSTACLE:
            self.obstacle_detected = True
            print("Obstacle detected ahead!")
            logging.warning(f"Obstacle ahead at position ({self.lane}, {self.position + 1})")
        else:
            self.obstacle_detected = False

    def display_status(self):
        """Display the robot's current status."""
        light = self.traffic_light.get_light_state(self.position)
        light_status = f"Traffic light: {light}" if light else "No traffic light"
        print(f"Position: Lane {self.lane}, {self.position} | Battery: {self.battery} | {light_status}")
        logging.info(f"Status -> Lane: {self.lane}, Position: {self.position}, Battery: {self.battery}")

# Simulation Class
class Simulation:
    def __init__(self, robot, road):
        self.robot = robot
        self.road = road
        self.running = True

    def run(self):
        """Run the simulation."""
        steps = 0
        while self.running and steps < 500:
            steps += 1
            print(f"\nStep {steps}:")
            self.robot.display_status()
            self.robot.scan_obstacle()

            if not self.robot.obstacle_detected:
                self.robot.move_forward()
            else:
                self.robot.make_decision()

            self.robot.traffic_light.update_lights()  # Update traffic lights every step
            time.sleep(0.5)  # Simulate time between actions

    def user_control(self):
        """Allow the user to control the robot through commands."""
        commands = ['forward', 'backward', 'left', 'right', 'stop']
        print("Manual mode. Available commands: forward, backward, left, right, stop.")
        
        while True:
            command = input("Enter command: ").lower()
            if command == 'forward':
                self.robot.move_forward()
            elif command == 'backward':
                self.robot.move_backward()
            elif command == 'left':
                self.robot.move_left()
            elif command == 'right':
                self.robot.move_right()
            elif command == 'stop':
                print("Stopping the robot.")
                self.running = False
                break
            else:
                print("Invalid command.")
            
            self.robot.display_status()
            self.robot.scan_obstacle()

# Main function to run the simulation
if __name__ == "__main__":
    # Initialize robot at the center lane, starting at the beginning of the road
    robot = Robot(lane=ROAD_WIDTH // 2, position=0)
    
    # Initialize simulation
    simulation = Simulation(robot, road)
    
    # Option to either run automatically or let the user control it
    mode = input("Choose mode: 'auto' for automated or 'manual' for user control: ").lower()
    
    if mode == 'auto':
        simulation.run()
    elif mode == 'manual':
        simulation.user_control()
    else:
        print("Invalid mode. Exiting.")
