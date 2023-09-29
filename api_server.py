from flask import Flask, jsonify, Response
from screeninfo import get_monitors
import cv2

app = Flask(__name__)

# Global Variables
cam = None
virtual_cam = None
latest_frame = None

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global cam, virtual_cam
    # Logic to start the virtual camera
    return jsonify({'message': 'Camera started'})

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global cam, virtual_cam
    # Logic to stop the virtual camera
    return jsonify({'message': 'Camera stopped'})

@app.route('/set_brightness/<value>', methods=['POST'])
def set_brightness(value):
    # Logic to adjust brightness
    return jsonify({'message': f'Brightness set to {value}'})

@app.route('/status', methods=['GET'])
def get_status():
    global cam, virtual_cam
    if cam and virtual_cam:
        return jsonify({'status': 'Camera is active'})
    return jsonify({'status': 'Camera is inactive'})

@app.route('/get_screens', methods=['GET'])
def get_screens():
    monitors = get_monitors()
    screen_names = [monitor.name for monitor in monitors]
    return jsonify(screen_names)

@app.route('/latest_frame', methods=['GET'])
def get_latest_frame():
    global latest_frame
    _, jpeg = cv2.imencode('.jpg', latest_frame)
    return Response(jpeg.tobytes(), content_type='image/jpeg')

if __name__ == '__main__':
    app.run(port=5000)
