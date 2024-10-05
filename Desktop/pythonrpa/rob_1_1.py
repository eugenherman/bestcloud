import math

class SpaceRobot:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.energy = 100  # Energy level for robot to perform actions
        print(f"Robot initialized at position ({self.x}, {self.y}, {self.z}).")

    def move(self, dx, dy, dz):
        """Move the robot by the given delta values along x, y, and z axes."""
        if self.energy > 0:
            self.x += dx
            self.y += dy
            self.z += dz
            self.energy -= 5  # Consuming energy for moving
            print(f"Robot moved to ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to move! Please recharge.")

    def current_position(self):
        """Return the robot's current coordinates."""
        return (self.x, self.y, self.z)

    def recharge(self):
        """Recharge the robot's energy."""
        self.energy = 100
        print("Energy recharged. Energy level: 100.")

    def distance_from(self, x, y, z):
        """Calculate the distance from the robot's current position to a target (x, y, z)."""
        dist = math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2)
        print(f"Distance from ({x}, {y}, {z}) is {dist:.2f}.")
        return dist

    def collect_sample(self):
        """Simulate the robot collecting a sample in space."""
        if self.energy > 10:
            self.energy -= 10
            print(f"Sample collected at ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to collect a sample! Please recharge.")

    def scan_area(self):
        """Simulate the robot scanning the surrounding area."""
        if self.energy > 15:
            self.energy -= 15
            print(f"Area scanned at ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to scan the area! Please recharge.")

# Example usage:
robot = SpaceRobot()

# Move the robot in 3D space
robot.move(5, 10, -2)
robot.move(-3, 4, 6)

# Check current position
print("Current position:", robot.current_position())

# Calculate distance from another point
robot.distance_from(10, 15, 5)

# Perform some actions
robot.collect_sample()
robot.scan_area()

# Recharge energy and perform another action
robot.recharge()
robot.collect_sample()
