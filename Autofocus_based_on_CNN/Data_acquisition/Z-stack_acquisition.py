# Import standard packages
import matplotlib.pyplot as plt
import numpy as np

# Import user packages
from modules.Move_Z import bipolar
from modules.Camera import capture_image_to_file


# Ask for resolution of images
resolution_key = input("Enter resolution variant:\n\
                        1280x720 -> 1\n\
                        1640x922 -> 2\n\
                        1920x1080 ->3\n\
                        3280x2464 ->4\n")
# Dictionary containing camera resolution modes
resolution_dict = {"1":(1280,720), "2":(1640,922),
                   "3":(1920,1080), "4":(3280,2464)}
# Variable storing required resolution
resolution = resolution_dict[resolution_key]

# Movement parameters: start, stop
start_step = 0
end = 20

# Ask for step mode
step_mode = input("Enter step mode:\n\
                   1 - with step = 2 um (micrometre)\n\
                   2 - with step = 10 um")
step_dict = {"1":1, "2":5}
# Variable storing required resolution
step = step_dict[step_mode]


# While-loop for continuous image acquisition process
while True:

    # Move up 
    for i in range(start, end + 1):
        # Capture image to file with name=step and required resolution
        capture_image_to_file(filename=str(i), resolution=resolution)
        # Print out message 
        print('Captured at', i)
        # Move one step up
        bipolar(step)
        
    # Return to focus position
    bipolar(-(i+1)*step)

    # Move down
    for i in range(start + 1, end + 1):
        # Move one step down
        bipolar(-div_step)
        # Capture image to file with name=step and required resolution
        Capture_image_to_file(filename=str(-i), resolution=resolution)
        # Print out message
        print('Captured at', -i)

    # Enter to continue
    print("Z-stack collected!")
    answer = input("Please enter yes/no to continue: ")
    
    # Check answer
    if answer == "yes":
        print("Choose next region of interest and make sure to focus the microscope")
    else:
        break
        
print("Process finished!")
