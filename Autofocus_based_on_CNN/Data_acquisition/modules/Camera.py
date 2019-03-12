# Import packages
from picamera import PiCamera
import time


def capture_image_to_file(filename, resolution):
	"""
	Function accepting filename to save an image 
	and resolution of an image as parameters.
	Function is used to capture images with 
	Raspberry Pi Camera Module V.2
	"""

    with PiCamera() as camera:
    	# Set resolution of an image
        camera.resolution = resolution
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        # Save image to folder on Raspberry Pi board
        camera.capture('/home/pi/Desktop/DB_collection/Temp/{}.jpg'.format(filename))


    
       
    
    



