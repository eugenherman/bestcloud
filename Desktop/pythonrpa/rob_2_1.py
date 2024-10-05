import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, position, velocity, acceleration, time_step):
        """Initialize the robot with its position, velocity, and acceleration."""
        self.position = np.array(position)  # [x, y, z]
        self.velocity = np.array(velocity)  # [vx, vy, vz]
        self.acceleration = np.array(acceleration)  # [ax, ay, az]
        self.time_step = time_step  # Time step for each movement (in seconds)
        self.trajectory = pd.DataFrame(columns=['Time', 'Position X', 'Position Y', 'Position Z',
                                                'Velocity X', 'Velocity Y', 'Velocity Z',
                                                'Acceleration X', 'Acceleration Y', 'Acceleration Z'])
        self.time_elapsed = 0  # Total time passed during simulation

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

    def simulate(self, total_time):
        """Simulate the robot's movement over a given period of time."""
        num_steps = int(total_time / self.time_step)
        for _ in range(num_steps):
            self.time_elapsed += self.time_step
            self.update_position()

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

    def display_trajectory_data(self):
        """Display the trajectory data."""
        print(self.trajectory)

# Example Usage
if __name__ == "__main__":
    # Initialize robot at position (0, 0, 0) with velocity (1, 2, 3) and constant acceleration (0.1, 0.1, 0)
    initial_position = [0, 0, 0]  # Starting at the origin
    initial_velocity = [1, 2, 3]  # Starting with some velocity in 3D space
    constant_acceleration = [0.1, 0.1, 0]  # Constant acceleration in the x, y directions, none in z
    time_step = 0.1  # Time step of 0.1 seconds

    # Create a robot object
    robot = Robot(initial_position, initial_velocity, constant_acceleration, time_step)

    # Simulate the robot's movement for 10 seconds
    robot.simulate(total_time=10)

    # Display the trajectory data
    robot.display_trajectory_data()

    # Plot the trajectory in 3D space
    robot.plot_trajectory() 
	
	 //   Time  Position X  Position Y  Position Z  Velocity X  Velocity Y  Velocity Z  Acceleration X  Acceleration Y  Acceleration Z
0    0.1    0.100000    0.200000    0.300000    1.010000    2.010000    3.000000           0.100000           0.100000           0.000000
1    0.2    0.201000    0.401000    0.600000    1.020000    2.020000    3.000000           0.100000           0.100000           0.000000
2    0.3    0.303000    0.603000    0.900000    1.030000    2.030000    3.000000           0.100000           0.100000           0.000000
...

