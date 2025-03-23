# 🤖 **Control Servo By Hand**

## 📋 **Overview**

This project demonstrates how to control a servo motor using hand gestures tracked via OpenCV, with HTTP requests sent to an ESP32 microcontroller. Adjust the servo motor’s angle in real-time based on your hand movements! Perfect for robotics 🤖, automation ⚙️, and IoT 🌐 applications.

### ⭐ **Features**

- ✋ Real-time hand gesture-based servo control.
- 👁️‍🗨️ Hand tracking powered by OpenCV.
- 🌐 HTTP requests to control ESP32.
- 🧑‍💻 Great for learning computer vision and IoT integration.

## 🧰 **Components Required**

- 🖥️ **ESP32 microcontroller**
- 🤖 **Servo motor** (e.g., SG90)
- 📷 **Camera** (USB webcam or laptop camera)
- 💻 **Computer** (Running Python with OpenCV)
- ⚡ **Power supply** (5V for the servo motor)

## 🛠️ **Installation and Usage**

### 1️⃣ **Clone the repository**

    git clone https://github.com/Manju200417/Control_Servo_By_Hand.git
    cd Control_Servo_By_Hand
2️⃣ Install the required dependencies
    
    pip install opencv-python requests
3️⃣ Circuit Connection
###  Connect the ESP32 to the **servo motor to the GPIO13 PIN** and camera as shown in the circuit diagram in the repository.
4️⃣ Run the Python script for hand gesture control

    python hand_control.py
This will start the hand gesture tracking process, and the detected hand positions will control the servo motor's angle via HTTP requests to the ESP32.

## 💻 **Code Explanation**

- 🖐️ **Hand Gesture Detection:** OpenCV captures video frames and detects hand gestures.
- 🔧 **Servo Control:** The hand position determines the servo angle.
- 🌐 **HTTP Communication:** HTTP requests are sent to the ESP32 to adjust the servo motor.

## 📦 **Dependencies**

- 🐍 **Python 3.x**
- 👁️ **OpenCV** (for hand gesture detection)
- 🔗 **Requests** (for sending HTTP requests)
- 🌐 **ESP32** (running a web server)

## 🚀 **Applications**

- 🎮 Gesture-controlled robotic arms
- 🤖 Touchless interfaces for automation
- 🖥️ Human-computer interaction experiments
- 🎓 Educational projects on computer vision and IoT

- ## 📦 **Sample Video**

https://github.com/user-attachments/assets/d138546e-ae52-47f6-997b-9c0e8bfe43f5

## 🤝 **Contributing**

Feel free to submit issues or pull requests to improve the project. Contributions are always welcome! 🎉

## 📜 **License**

This project is open-source and available under the MIT License.

## 📧 **Contact**

For questions or collaborations, reach out via [GitHub Issues]
