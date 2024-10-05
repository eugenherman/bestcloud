import math
import random

class SpaceRobot:
    def __init__(self, x=0, y=0, z=0):
        """Initialize the robot at the specified (x, y, z) coordinates."""
        self.x = x
        self.y = y
        self.z = z
        self.energy = 100  # Initial energy level
        self.max_energy = 100
        self.obstacles = []  # List to store obstacles in space
        print(f"Robot initialized at position ({self.x}, {self.y}, {self.z}) with energy {self.energy}.")

    def move(self, dx, dy, dz):
        """Move the robot by the given delta values in 3D space."""
        if self.energy <= 0:
            print("Not enough energy to move! Please recharge.")
            return
        
        new_x = self.x + dx
        new_y = self.y + dy
        new_z = self.z + dz
        
        if self.detect_obstacle(new_x, new_y, new_z):
            print("Obstacle detected! Cannot move in the desired direction.")
            return
        
        self.x = new_x
        self.y = new_y
        self.z = new_z
        self.energy -= 5  # Consumes energy for movement
        print(f"Robot moved to ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        
        if self.energy <= 10:
            print("Warning: Low energy! Recharge soon.")
        
    def navigate_to(self, target_x, target_y, target_z):
        """Move the robot to the specified target coordinates in steps."""
        print(f"Navigating to ({target_x}, {target_y}, {target_z})...")
        while (self.x, self.y, self.z) != (target_x, target_y, target_z):
            dx = (target_x - self.x) / abs(target_x - self.x) if target_x != self.x else 0
            dy = (target_y - self.y) / abs(target_y - self.y) if target_y != self.y else 0
            dz = (target_z - self.z) / abs(target_z - self.z) if target_z != self.z else 0
            
            self.move(dx, dy, dz)
            
            if self.energy <= 0:
                print("Robot out of energy while navigating!")
                break

    def detect_obstacle(self, x, y, z):
        """Detect if there's an obstacle at the given coordinates."""
        for obstacle in self.obstacles:
            if (x, y, z) == obstacle:
                return True
        return False

    def add_obstacle(self, x, y, z):
        """Add an obstacle at the specified coordinates."""
        self.obstacles.append((x, y, z))
        print(f"Obstacle added at ({x}, {y}, {z}).")

    def recharge(self):
        """Recharge the robot's energy to maximum."""
        self.energy = self.max_energy
        print("Robot recharged to full energy.")

    def collect_sample(self):
        """Simulate collecting a sample in space."""
        if self.energy >= 10:
            self.energy -= 10
            print(f"Sample collected at ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to collect a sample! Please recharge.")

    def scan_area(self):
        """Simulate scanning the area around the robot."""
        if self.energy >= 15:
            self.energy -= 15
            print(f"Area scanned around ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to scan the area! Please recharge.")
    
    def repair_module(self):
        """Simulate repairing a nearby module."""
        if self.energy >= 20:
            self.energy -= 20
            print(f"Module repaired at ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to repair module! Please recharge.")

    def build_structure(self):
        """Simulate building a structure at the current location."""
        if self.energy >= 25:
            self.energy -= 25
            print(f"Structure built at ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to build structure! Please recharge.")
    
    def transmit_data(self):
        """Simulate transmitting data to the base."""
        if self.energy >= 5:
            self.energy -= 5
            print(f"Data transmitted from ({self.x}, {self.y}, {self.z}). Remaining energy: {self.energy}.")
        else:
            print("Not enough energy to transmit data! Please recharge.")
    
    def auto_avoid_obstacle(self, target_x, target_y, target_z):
        """Autonomously navigate around obstacles to reach the target."""
        print(f"Auto-navigating to ({target_x}, {target_y}, {target_z}) avoiding obstacles...")
        while (self.x, self.y, self.z) != (target_x, target_y, target_z):
            dx = (target_x - self.x) / abs(target_x - self.x) if target_x != self.x else 0
            dy = (target_y - self.y) / abs(target_y - self.y) if target_y != self.y else 0
            dz = (target_z - self.z) / abs(target_z - self.z) if target_z != self.z else 0
            
            if not self.detect_obstacle(self.x + dx, self.y + dy, self.z + dz):
                self.move(dx, dy, dz)
            else:
                print("Obstacle detected, re-routing...")
                # Try different route
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1])
                dz = random.choice([-1, 0, 1])
                self.move(dx, dy, dz)
            
            if self.energy <= 0:
                print("Robot out of energy while auto-navigating!")
                break

# Example Usage

# Create a space robot at an initial position
robot = SpaceRobot(0, 0, 0)

# Add some obstacles in the 3D space
robot.add_obstacle(3, 3, 3)
robot.add_obstacle(5, 5, 5)

# Move and perform actions
robot.move(2, 2, 2)
robot.collect_sample()

# Try to navigate to a specific position
robot.navigate_to(5, 5, 5)

# Scan area and build a structure
robot.scan_area()
robot.build_structure()

# Transmit data back to base
robot.transmit_data()

# Recharge and continue
robot.recharge()
robot.repair_module()

# Auto-navigate with obstacle avoidance
robot.auto_avoid_obstacle(10, 10, 10)
