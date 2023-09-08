# zoom-virtual-overlay

Overlay your camera feed on a desktop screengrab and stream it to a virtual webcam for Zoom calls. 

## Features

- Captures a live desktop screengrab.
- Overlays a live camera feed on the screengrab.
- Streams the combined feed to a virtual webcam.
- Use this virtual webcam as your video source in Zoom or any other video conferencing tool.

## Prerequisites

- Docker installed on your system.
- Python 3.8 or higher.
- Webcam for capturing live video feed.

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Cdaprod/zoom-virtual-overlay.git
   cd zoom-virtual-overlay
   ```

2. **Build the Docker Container**:
   ```bash
   docker build -t zoom-virtual-cam .
   ```

3. **Run the Container**:
   ```bash
   docker run zoom-virtual-cam
   ```

## Usage

1. Start the virtual webcam by running the Docker container.
2. Open Zoom or any other video conferencing tool.
3. Go to settings and select the virtual webcam as your video source.
4. Enjoy your enhanced video feed with a desktop screengrab overlay!

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements, bugs, or suggestions.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact

- Github: [@Cdaprod](https://github.com/Cdaprod)
- Twitter: [@cdasmktcda](https://twitter.com/cdasmktcda)
- LinkedIn: [cdasmkt](https://www.linkedin.com/in/cdasmkt/)
- Blog: [Sanity.Cdaprod.dev](https://Sanity.Cdaprod.dev)

#devopsdad #tripletdad #hacktheplanet

---

Feel free to customize the README.md as per your requirements and add more sections if needed.