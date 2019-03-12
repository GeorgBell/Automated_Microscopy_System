# Import standard packages
import RPi.GPIO as GPIO
from time import sleep

def bipolar(steps):
    """
    Function accepts number of steps that the motor should move.
    Function utilizes package to access GPIO pins of Raspberry Pi
    board used to connect stepper motor through driver.
    """       
    
    # Set pins
    ENBL_Z = 26  # Pin used to enable driver's workflow
    # Set pins used to choose the step chopping mode
    M0_Z = 21    
    M1_Z = 20
    M2_Z = 16
    DIR_Z = 13   # Direction pin
    STEP_Z = 19  # Step pin
    
    # Set subsidiary variables 
    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    SPR = 200   # Steps per Revolution (360 / angle)

    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR_Z, GPIO.OUT)
    GPIO.setup(STEP_Z, GPIO.OUT)
    GPIO.setup(ENBL_Z, GPIO.OUT)

    # Enable stepper motor driver
    GPIO.output(ENBL_Z, GPIO.LOW) 

    # Microstep resolution GPIO Pins
    MODE = (M0_Z, M1_Z, M2_Z)   
    GPIO.setup(MODE, GPIO.OUT)
    RESOLUTION = {'Full': (0, 0, 0),
                  'Half': (1, 0, 0),
                  '1/4': (0, 1, 0),
                  '1/8': (1, 1, 0),
                  '1/16': (0, 0, 1),
                  '1/32': (1, 0, 1)}
    # Use 1/32 microstep resolution
    GPIO.output(MODE, RESOLUTION['1/32'])

    # Set movement parameters 
    # One step size
    step_count = int(SPR*abs(steps))
    # Time interval between movements    
    delay = .0208/128

    # Define direction of movements
    if (steps steps>= 0):
    	# Clockwise rotation
    	GPIO.output(DIR_Z, CW)
    	# For-loop of step movements
        for x in range(step_count):
            GPIO.output(STEP_Z, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay)
    else:
        # Counterlockwise rotation
        GPIO.output(DIR_Z, CCW)
        # For-loop of step movements
        for x in range(step_count):
            GPIO.output(STEP_Z, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP_Z, GPIO.LOW)
            sleep(delay)      
    
    # Clean GPIO pins
    GPIO.cleanup()


