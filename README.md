VolumeHandControl
*Description
VolumeHandControl is an innovative Python application designed to let you control your computer’s audio volume using simple hand gestures detected by your webcam. Leveraging Google’s MediaPipe for real-time hand tracking combined with OpenCV’s powerful computer vision capabilities, this app measures the distance between your thumb and index finger to adjust your system volume smoothly and intuitively.

No physical buttons or keyboards are needed — just move your fingers in front of your camera to increase or decrease volume effortlessly. This solution offers a modern, touchless way to interact with your PC, ideal for multitasking, presentations, or when your hands are occupied.

The application uses the pycaw library to interface with Windows audio sessions, ensuring precise and system-wide volume control. The graphical interface provides visual feedback on the detected finger positions, current volume level, and frame rate, making it easy to monitor performance and usage in real time.




*Features

-Real-time hand detection and tracking using MediaPipe

-Volume control based on finger distance measurement

-Visual feedback with OpenCV window showing finger landmarks, volume bar, and FPS

-Smooth and responsive volume adjustments via pycaw (Windows only)

-Simple Tkinter-based GUI launcher for starting and exiting the app


*Installation on Windows

Step 1: Clone the repository
Open Command Prompt or PowerShell and run:

*git clone https://github.com/YOUR_USERNAME/VolumeHandControl.git
*cd VolumeHandControl


Step 2: Create and activate a virtual environment (recommended)

python -m venv mp-env
mp-env\Scripts\activate


Step 3: Install required Python packages

pip install opencv-python mediapipe numpy pycaw comtypes


Step 4: Run the GUI application

python gui.py



