import numpy as np

class SimpleSensor:
    """A simple sensor that detects a line on the floor."""
    
    def __init__(self, position_noise=0.1):
        self.position_noise = position_noise
    
    def detect_line(self, robot_x, robot_y, line_equation):
        """
        Detect the position of a line relative to the robot.
        
        Args:
            robot_x, robot_y: Current position of the robot
            line_equation: Function that represents the line (y = f(x))
        
        Returns:
            relative_position: How far the line is from the robot (positive = right, negative = left)
        """
        true_line_y = line_equation(robot_x)
        sensor_reading = true_line_y - robot_y
        
        # Add some noise to simulate real-world sensor inaccuracies
        noisy_reading = sensor_reading + np.random.normal(0, self.position_noise)
        
        return noisy_reading

# Example usage
if __name__ == "__main__":
    sensor = SimpleSensor(position_noise=0.05)

    # Define a simple line: y = 0.5x + 2
    line_fn = lambda x: 0.5 * x + 2

    # Robot position
    robot_x, robot_y = 1.0, 1.2

    line_position = sensor.detect_line(robot_x, robot_y, line_fn)
    print(f"Robot at ({robot_x}, {robot_y}), Line detected at relative position: {line_position:.3f}")