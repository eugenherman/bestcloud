import numpy as np
import pygame
from pygame.locals import *

# Setup display window for simulation
width, height = 800, 600
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Robot Simulation")

# Robot parameters
class Robot3D:
    def __init__(self):
        # Joint angles in degrees
        self.joint_angles = np.zeros(3)  # [Base, Shoulder, Elbow]

        # Link lengths
        self.link_lengths = [100, 150, 100]

    def forward_kinematics(self):
        """
        Calculate the 3D position of the robot's end effector using the joint angles.
        """
        base_angle = np.radians(self.joint_angles[0])
        shoulder_angle = np.radians(self.joint_angles[1])
        elbow_angle = np.radians(self.joint_angles[2])

        # First link transformation
        x1 = self.link_lengths[0] * np.cos(base_angle)
        y1 = self.link_lengths[0] * np.sin(base_angle)
        z1 = 0  # Base link is always at ground level

        # Second link transformation
        x2 = x1 + self.link_lengths[1] * np.cos(shoulder_angle) * np.cos(base_angle)
        y2 = y1 + self.link_lengths[1] * np.cos(shoulder_angle) * np.sin(base_angle)
        z2 = self.link_lengths[1] * np.sin(shoulder_angle)

        # Third link transformation (end-effector)
        x3 = x2 + self.link_lengths[2] * np.cos(elbow_angle) * np.cos(shoulder_angle)
        y3 = y2 + self.link_lengths[2] * np.cos(elbow_angle) * np.sin(shoulder_angle)
        z3 = z2 + self.link_lengths[2] * np.sin(elbow_angle)

        return [(0, 0, 0), (x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]

    def rotate_joint(self, joint_index, angle):
        """
        Rotate a given joint by a specified angle in degrees.
        """
        self.joint_angles[joint_index] += angle
        self.joint_angles[joint_index] = np.clip(self.joint_angles[joint_index], -180, 180)

# Visualization function
def draw_robot(screen, points):
    """
    Draw a simple 3D robot arm based on the 3D points.
    For simplicity, we project the 3D points onto a 2D surface.
    """
    def project_3d_to_2d(point):
        # Basic orthographic projection, we ignore z-axis for simplicity
        scale = 400 / (point[2] + 500)  # To prevent division by zero and create depth
        x2d = width / 2 + int(point[0] * scale)
        y2d = height / 2 - int(point[1] * scale)
        return x2d, y2d

    # Convert 3D points to 2D
    points_2d = [project_3d_to_2d(point) for point in points]

    # Draw the robot links
    pygame.draw.line(screen, (0, 255, 0), points_2d[0], points_2d[1], 5)  # Base to Shoulder
    pygame.draw.line(screen, (0, 255, 0), points_2d[1], points_2d[2], 5)  # Shoulder to Elbow
    pygame.draw.line(screen, (0, 255, 0), points_2d[2], points_2d[3], 5)  # Elbow to End-Effector

# Simulation loop
def simulation():
    clock = pygame.time.Clock()
    robot = Robot3D()

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Control the robot using arrow keys
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            robot.rotate_joint(0, -1)  # Rotate base joint
        if keys[K_RIGHT]:
            robot.rotate_joint(0, 1)
        if keys[K_UP]:
            robot.rotate_joint(1, -1)  # Rotate shoulder joint
        if keys[K_DOWN]:
            robot.rotate_joint(1, 1)
        if keys[K_q]:
            robot.rotate_joint(2, -1)  # Rotate elbow joint
        if keys[K_e]:
            robot.rotate_joint(2, 1)

        # Get current joint positions in 3D space
        points = robot.forward_kinematics()

        # Draw robot
        draw_robot(screen, points)

        pygame.display.flip()
        clock.tick(60)  # Run at 60 FPS

    pygame.quit()

if __name__ == '__main__':
    simulation()
