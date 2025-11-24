🖱️ AI Virtual Mouse System -- README
====================================

📌 Overview
-----------

The **AI Virtual Mouse System** is a computer vision--based human--computer interaction project that allows users to **control the mouse cursor using hand gestures**.\
It uses **OpenCV**, **MediaPipe**, **NumPy**, **PyAutoGUI**, and **Autopy** to track hand landmarks and translate gestures into mouse actions such as:

-   Cursor movement

-   Left click

-   Right click

-   Scrolling

-   Gesture recognition

This eliminates the need for a physical mouse and demonstrates how AI can enhance natural interaction with computers.

* * * * *

🛠️ Technologies Used
---------------------

| Library / Framework | Purpose |
| --- | --- |
| **Python 3.11** | Main programming language |
| **OpenCV** | Webcam input and image processing |
| **MediaPipe Hands** | Hand landmark detection |
| **NumPy** | Coordinate mapping & interpolation |
| **PyAutoGUI** | Mouse control, scrolling & right-click |
| **Autopy** | High-precision mouse movement |

All core logic for hand tracking is implemented in:\
📄 **HandTracking.py** (gesture detection and landmark extraction)

HandTracking\
📄 **mouse.py** (gesture-to-mouse action mapping)

mouse

* * * * *

📁 Project Structure
--------------------

`AI-Virtual-Mouse/
│── HandTracking.py   # Hand detection & utility functions
│── mouse.py          # Main virtual mouse program
│── README.md         # Documentation`

* * * * *

⚙️ Installation & Setup
-----------------------

### 1\. Install Python

Install Python 3.10--3.11 (recommended).

### 2\. Install Required Libraries

Run:

`pip install opencv-python mediapipe numpy autopy pyautogui`

If PyAutoGUI gives failsafe errors, it is disabled in the code using:

`pyautogui.FAILSAFE = False`

### 3\. Connect Webcam

Ensure your laptop/PC webcam is working.

### 4\. Run the Virtual Mouse

`python mouse.py`

* * * * *

✋ Hand Gesture Controls
-----------------------

### 🎯 1. **Move Mouse Cursor**

-   Gesture: **Only index finger up**

-   Action: Move cursor smoothly across screen

### 🖱️ 2. **Left Click**

-   Gesture: Index finger + Middle finger **close together**

-   Action: Left mouse click

### ➡️ 3. **Right Click**

-   Gesture: Index + Middle + Ring finger UP, Pinky DOWN

-   Action: Right-click

### 📜 4. **Scrolling**

-   Gesture: All four fingers UP

-   Small distance between index & middle: Scroll down

-   Large distance: Scroll up

* * * * *

🔍 How It Works (Behind the Scenes)
-----------------------------------

### 📌 Step 1 --- Hand Detection (MediaPipe)

From **HandTracking.py**, MediaPipe detects 21 hand landmarks.\
Key functions used:

-   `findHands()` → Detects hand

-   `findPosition()` → Extracts landmark coordinates

-   `fingersUp()` → Checks which fingers are raised

-   `findDistance()` → Calculates distance between two fingers

### 📌 Step 2 --- Gesture Recognition

From **mouse.py**, gestures are identified by analyzing which fingers are raised.

Example:

`if fingers[1] == 1 and fingers[2] == 0:
    # move cursor`

### 📌 Step 3 --- Screen Mapping

Finger coordinates (camera space) → Screen coordinates using:

`np.interp()`

### 📌 Step 4 --- Mouse Movement

Cursor is moved smoothly:

`autopy.mouse.move()`

Scrolling & clicks are done via:

`pyautogui.click()
pyautogui.scroll()`

* * * * *

🎥 Screenshot (Conceptual Workflow)
-----------------------------------

 `Webcam → OpenCV → MediaPipe → Finger Tracking → Gesture Logic → Mouse Actions`

* * * * *

🚀 Features
-----------

✔ Hands-free mouse control\
✔ Real-time gesture tracking (30--60 FPS)\
✔ Accurate hand landmark detection\
✔ Smooth cursor movement\
✔ Click, scroll, and right-click support\
✔ Works on any laptop/PC with webcam

* * * * *

🛠️ Future Improvements
-----------------------

-   Add drag & drop gesture

-   Add volume control with gestures

-   Add double-click gesture

-   Add multi-hand interaction

-   Add GUI for customization

* * * * *

📌 Conclusion
-------------

The **AI Virtual Mouse System** demonstrates how computer vision and machine learning can replace traditional hardware with smart gesture-based interfaces.\
It is a powerful application for:

-   Accessibility

-   Touchless systems

-   Human--computer interaction research

-   Gesture-based automation