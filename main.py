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
        # Capture the screengrab
        screengrab = pygame.surfarray.array3d(pygame.display.get_surface())

        # Capture the camera feed
        ret, frame = cam.read()

        # Resize the camera feed to match the screengrab dimensions
        frame = cv2.resize(frame, (width, height))

        # Overlay the camera feed on the screengrab
        overlay = cv2.addWeighted(frame, 0.5, screengrab, 0.5, 0)

        # Convert the overlayed image to RGB format for PyGame
        overlay_rgb = cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB)

        # Display the overlayed image
        pygame.surfarray.blit_array(screen, overlay_rgb)
        pygame.display.flip()

        # Send the overlayed image to the virtual camera
        virtual_cam.send(overlay_rgb)

        # Handle keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the program if the window is closed
                cam.release()
                cv2.destroyAllWindows()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # Quit the program if 'q' is pressed
                    cam.release()
                    cv2.destroyAllWindows()
                    pygame.quit()
                    exit()



    
    
import numpy as np
import cv2

# Convert an image from RGB to Grayscale
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Resize an image to the specified dimensions
def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

# Rotate an image by the specified angle
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

# Adjust the brightness of an image
def adjust_brightness(image, value=1.0):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv[:, :, 2] = hsv[:, :, 2] * value
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

