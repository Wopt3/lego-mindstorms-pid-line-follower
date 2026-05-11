from mindstorms import MSHub, MotorPair, ColorSensor
from mindstorms.control import wait_for_seconds
from mindstorms.control import Timer

# ============================================================
# LEGO Mindstorms - Line Following Robot with PID Controller
# ============================================================
# Project description:
# The robot follows a marked line using a color sensor.
# The blue component of the reflected light is used as feedback.
# A PID controller calculates the correction value, which is then
# applied to the motor power to keep the robot close to the line.
# ============================================================


# -----------------------------
# Hardware configuration
# -----------------------------

# Pair of driving motors connected to ports A and B
motor_AB = MotorPair('A', 'B')

# Color sensor connected to port F
color_sensor = ColorSensor('F')


# -----------------------------
# PID controller parameters
# -----------------------------

# Base motor power
# This value defines the default speed of the robot.
BASE_POWER = 25

# PID gains
# Kp - proportional gain: reacts to the current error
# Ki - integral gain: reacts to the accumulated error over time
# Kd - derivative gain: reacts to the rate of error change
Kp = 0.02
Ki = 0.0003
Kd = 0.00005

# Target sensor value
# This is the reference value that the robot tries to maintain.
# It should be adjusted experimentally for the selected track.
TARGET_BLUE_VALUE = 350


# -----------------------------
# PID internal variables
# -----------------------------

integral = 0
last_error = 0


# -----------------------------
# Main control loop
# -----------------------------

# Run the robot 
while true:

    # Read the blue component from the color sensor
    current_blue_value = color_sensor.get_blue()

    # Calculate the control error
    # Positive or negative value shows how far the robot is
    # from the desired color/reference value.
    error = current_blue_value - TARGET_BLUE_VALUE

    # Integral part
    # Accumulates the error over time and helps eliminate
    # long-term deviation from the desired track.
    integral += error

    # Derivative part
    # Measures how quickly the error changes.
    derivative = error - last_error

    # PID correction calculation
    correction = (Kp * error) + (Ki * integral) + (Kd * derivative)

    # Motor power calculation
    # One motor receives more power and the other less power,
    # which causes the robot to turn left or right.
    power_left = BASE_POWER + correction
    power_right = BASE_POWER - correction

    # Save current error for the next loop iteration
    last_error = error

    # Start motors using tank steering
    # Negative values are used because of the motor orientation
    # in the robot construction.
    motor_AB.start_tank_at_power(
        int(-power_left),
        int(-power_right)
    )

    # Short delay to stabilize sensor readings and control loop
    wait_for_seconds(0.05)

