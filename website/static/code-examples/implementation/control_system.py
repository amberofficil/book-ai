import numpy as np
import matplotlib.pyplot as plt

class PIDController:
    """A simple PID (Proportional-Integral-Derivative) controller for robot control."""
    
    def __init__(self, kp, ki, kd, dt=0.01):
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        self.dt = dt  # Time step
        
        self.previous_error = 0
        self.integral_error = 0
    
    def compute(self, setpoint, measured_value):
        """Compute the control signal."""
        error = setpoint - measured_value
        
        # Proportional term
        p_term = self.kp * error
        
        # Integral term
        self.integral_error += error * self.dt
        i_term = self.ki * self.integral_error
        
        # Derivative term
        derivative = (error - self.previous_error) / self.dt
        d_term = self.kd * derivative
        
        # Save current error for next iteration
        self.previous_error = error
        
        # Compute output
        output = p_term + i_term + d_term
        return output

class RobotSimulator:
    """A simple robot simulator with position control."""
    
    def __init__(self, initial_position=0.0, initial_velocity=0.0):
        self.position = initial_position
        self.velocity = initial_velocity
        self.mass = 1.0  # Robot mass
        self.friction = 0.1  # Friction coefficient
    
    def update(self, control_signal, dt=0.01):
        """Update robot state based on control signal."""
        # Apply control signal as force
        force = control_signal
        
        # Apply friction
        friction_force = -self.friction * self.velocity
        total_force = force + friction_force
        
        # Calculate acceleration (F = ma => a = F/m)
        acceleration = total_force / self.mass
        
        # Update velocity and position
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

# Example: Control a robot to reach a target position
if __name__ == "__main__":
    target_position = 10.0
    current_position = 0.0

    # Initialize PID controller
    pid = PIDController(kp=2.0, ki=0.1, kd=0.05)

    # Initialize robot
    robot = RobotSimulator(initial_position=current_position)

    # Simulation parameters
    dt = 0.01
    simulation_time = 10.0  # seconds
    steps = int(simulation_time / dt)

    # Store history for plotting
    time_history = []
    position_history = []
    target_history = []

    for step in range(steps):
        time = step * dt
        
        # Compute control signal
        control_signal = pid.compute(target_position, robot.position)
        
        # Update robot
        robot.update(control_signal, dt)
        
        # Store history
        time_history.append(time)
        position_history.append(robot.position)
        target_history.append(target_position)
        
        # Check if we've reached the target (with tolerance)
        if abs(robot.position - target_position) < 0.1:
            print(f"Target reached at time {time:.2f}s")
            break

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(time_history, position_history, label='Robot Position', linewidth=2)
    plt.plot(time_history, target_history, label='Target Position', linestyle='--', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.title('PID Control of Robot Position')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Final position: {robot.position:.3f}, Target: {target_position}")