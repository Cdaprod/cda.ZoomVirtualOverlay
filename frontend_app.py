import streamlit as st
import requests
import pygetwindow as gw
import numpy as np
import cv2

st.title('Video Connection Manager')

# Start/stop the virtual camera
if st.button('Start Camera'):
    response = requests.post('http://localhost:5000/start_camera')
    st.write(response.json()['message'])

if st.button('Stop Camera'):
    response = requests.post('http://localhost:5000/stop_camera')
    st.write(response.json()['message'])

# Adjust brightness
brightness = st.slider('Adjust Brightness', 0.5, 1.5, 1.0)
if st.button('Set Brightness'):
    response = requests.post(f'http://localhost:5000/set_brightness/{brightness}')
    st.write(response.json()['message'])

# Display camera status
response = requests.get('http://localhost:5000/status')
st.write(response.json()['status'])

# Fetch and display available screens
response = requests.get('http://localhost:5000/get_screens')
screens = response.json()
selected_screen = st.selectbox('Choose a screen to capture:', screens)

# Position overlay
overlay_position = st.slider('Position Overlay (X, Y)', (0, 0), (640, 480), (0, 0))
# TODO: Incorporate the overlay_position in the video processing logic

# Display the content of the selected screen
if st.button('Show Selected Screen'):
    screen = gw.getWindowsWithTitle(selected_screen)[0]
    screen_np = np.array(screen._hWndDC)
    st.image(screen_np, caption='Captured Screen', use_column_width=True)
