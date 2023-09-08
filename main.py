import cv2
import pygame
import pyvirtualcam
import numpy as np

# Set the dimensions of the screen
width = 640
height = 480

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((width, height))

# Initialize the camera
cam = cv2.VideoCapture(0)

# Initialize virtual camera
with pyvirtualcam.Camera(width=width, height=height, fps=20) as virtual_cam:
    while True:
        # ... [rest of the code remains unchanged]
        
        # Send the overlayed image to the virtual camera
        virtual_cam.send(overlay_rgb)
        
        # Sleep for a short duration before capturing the next frame
        virtual_cam.sleep_until_next_frame()

        # ... [rest of the code remains unchanged]
