import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import minimize

class Robot:
    def __init__(self, position, velocity, acceleration, mass, time_step):
        """Initialize the robot with position, velocity, acceleration, and mass."""
        self.position = np.array(position)  # [x, y, z]
        self.velocity = np.array(velocity)  # [vx, vy, vz]
        self.acceleration = np.array(acceleration)  # [ax, ay, az]
        self.mass = mass  # Mass of the robot (important for forces)
        self.time_step = time_step  # Time step for each movement (in seconds)
        self.trajectory = pd.DataFrame(columns=['Time', 'Position X', 'Position Y', 'Position Z',
                                                'Velocity X', 'Velocity Y', 'Velocity Z',
                                                'Acceleration X', 'Acceleration Y', 'Acceleration Z'])
        self.time_elapsed = 0  # Total time passed during simulation

    def apply_force(self, force):
        """Calculate the acceleration from the applied force using F = ma."""
        self.acceleration = force / self.mass

    def update_position(self):
        """Update the position of the robot based on its velocity and acceleration."""
        # Update the velocity using the formula: v = u + at
        self.velocity += self.acceleration * self.time_step
        
        # Update the position using the formula: s = s0 + vt
        self.position += self.velocity * self.time_step

        # Log the trajectory into the Pandas DataFrame
        self.log_trajectory()

    def log_trajectory(self):
        """Log the robot's current state into the trajectory DataFrame."""
        row = {'Time': self.time_elapsed,
               'Position X': self.position[0], 'Position Y': self.position[1], 'Position Z': self.position[2],
               'Velocity X': self.velocity[0], 'Velocity Y': self.velocity[1], 'Velocity Z': self.velocity[2],
               'Acceleration X': self.acceleration[0], 'Acceleration Y': self.acceleration[1], 'Acceleration Z': self.acceleration[2]}
        self.trajectory = self.trajectory.append(row, ignore_index=True)

    def simulate(self, total_time, external_forces=None):
        """Simulate the robot's movement over a given period of time."""
        num_steps = int(total_time / self.time_step)
        for i in range(num_steps):
            self.time_elapsed += self.time_step
            # Optionally apply external forces (which can vary over time)
            if external_forces:
                force = external_forces(self.time_elapsed)
                self.apply_force(force)
            self.update_position()

    def display_trajectory_data(self):
        """Display the trajectory data."""
        print(self.trajectory)

    def plot_trajectory(self):
        """Plot the robot's 3D trajectory using matplotlib."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Extract position columns
        x = self.trajectory['Position X']
        y = self.trajectory['Position Y']
        z = self.trajectory['Position Z']

        ax.plot(x, y, z, label='Trajectory', marker='o')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Z Position')
        ax.set_title('3D Trajectory of the Robot')
        plt.legend()
        plt.show()

    def optimize_trajectory(self, target_position):
        """Optimize the trajectory to reach a target position by minimizing the distance."""
        def distance_from_target(params):
            # params = [vx, vy, vz] (initial velocity)
            velocity = np.array(params)
            final_position = self.simulate_until_target(velocity, target_position)
            distance = np.linalg.norm(final_position - target_position)
            return distance

        # Initial guess for velocity
        initial_guess = self.velocity

        # Perform optimization
        result = minimize(distance_from_target, initial_guess, method='BFGS')
        print(f"Optimized velocity: {result.x}")
        return result.x

    def simulate_until_target(self, velocity, target_position, max_time=100):
        """Simulate the robot's movement until it reaches the target position or max_time is reached."""
        self.velocity = velocity
        num_steps = int(max_time / self.time_step)
        for i in range(num_steps):
            self.time_elapsed += self.time_step
            self.update_position()
            if np.linalg.norm(self.position - target_position) < 0.01:  # Close enough to the target
                break
        return self.position


# Define external forces (gravity, random perturbations, etc.)
def external_forces(time):
    """Example of a force function that changes over time."""
    # Simulating gravitational force along the z-axis and random perturbation in x, y directions
    gravity = np.array([0, 0, -9.8])  # Gravity in the z direction
    random_perturbation = np.array([np.random.normal(0, 0.1), np.random.normal(0, 0.1), 0])
    return gravity * 10 + random_perturbation


# Example Usage
if __name__ == "__main__":
    # Initialize robot at position (0, 0, 0) with velocity (1, 2, 3), constant acceleration (0, 0, 0), and mass 1 kg
    initial_position = [0, 0, 0]
    initial_velocity = [1, 2, 3]
    initial_acceleration = [0, 0, 0]  # Starting with no acceleration
    mass = 1.0  # kg
    time_step = 0.1  # seconds

    # Create a robot object
    robot = Robot(initial_position, initial_velocity, initial_acceleration, mass, time_step)

    # Simulate the robot's movement for 30 seconds with external forces
    robot.simulate(total_time=30, external_forces=external_forces)

    # Display the trajectory data
    robot.display_trajectory_data()

    # Plot the trajectory in 3D space
    robot.plot_trajectory()

    # Optimize the trajectory to reach a target position
    target_position = np.array([10, 10, 0])  # Example target position
    robot.optimize_trajectory(target_position)

    # Simulate until reaching the target position
    robot.simulate_until_target(robot.velocity, target_position)
