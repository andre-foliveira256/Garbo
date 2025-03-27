# Garbo - Smart Ecopoint  

## The Problem

Waste sorting at home is essential for effective recycling, yet many households struggle with properly separating materials, leading to contamination and inefficient waste management. Traditional recycling bins do not provide any guidance or automation, making the process inconvenient for users.  

## Project Overview  

Our idea is to develop **Garbo**, a **Smart Ecopoint**, an intelligent recycling system that automates waste sorting at home. Using **AI-powered cameras**, our system classifies different types of waste, specificallly paper and plastic, ensuring proper disposal. The system will also **notify users when bins are full**, optimizing disposal routines. This product is targeted at **households and waste management companies**, improving recycling efficiency and reducing environmental impact.  

---

## General Information  

The Smart Ecopoint was implemented using a cardboard structure with a trapdoor mechanism made from a stick and an attached paper flap. This trapdoor is connected to a DC motor, which controls its movement. A camera trained with a custom dataset detects two types of waste: paper and plastic. When an item is placed in the system, the camera identifies its material. The DC motor then rotates the stick, moving the trapdoor to block the incorrect bin, ensuring the garbage falls into the correct one.

This system addresses the issue of people resisting waste separation due to the extra effort required. By automating the process, our solution simplifies recycling, making it more convenient for households.
---

## Built With  

This section outlines the technologies used in the project, including hardware components, software dependencies, and tools.  

### **Hardware**  

- [Nicla Vision](https://store.arduino.cc/products/nicla-vision)(https://docs.arduino.cc/hardware/nicla-vision/) - AI-powered camera for object detection  

- [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - Embedded system to work as a middleman between the camera and the arduino so they can receive messages from each other more specifically from the camera to the arduino.

- [DC Motor](https://www.ptrobotics.com/motor-dc/2349-hobby-motor-gear.html?gad_source=1&gclid=EAIaIQobChMIoY-0oMGqjAMV0jwGAB0vVwz5EAQYBSABEgJusvD_BwE) - Motor for trapdoor control 

- [Arduino Uno](https://store.arduino.cc/en-pt/products/arduino-uno-rev3?srsltid=AfmBOorFwxpVc0hA0pXcm9r8AjatWzmVzfhsLIPbAOYZjzseUJMvptUe) - System that connects and control the dc motor

### **Software**  

- [Raspberry Pi OS](https://www.raspberrypi.com/software/) - Operating System  
- [Python](https://www.python.org/) - Main programming language used to program the code of the camera [camera code](/C04_solution/camera/Object_detection_send_data.py) and the script that allows the communication between the camera and the arduino [script](/C04_solution/script.py)
- [OpenMV](https://openmv.io/) - IDE used to program the code of the camera
- [Edge Impulse](https://www.edgeimpulse.com/) - Machine learning model training used to train the camera 
- [Arduino Programming Language](https://docs.arduino.cc/language-reference/) - C/C++ adaptation used to 
- [Arduino IDE](https://www.arduino.cc/en/software) - Used to program the behaviour of the dc motor [motor code](/C04_solution/motor/motor.ino)
- [Gotify](https://gotify.net/)(https://github.com/gotify) - Used to implement the notification aspect of the project
- [Visual Studio](https://code.visualstudio.com/) - Used to create and edit the script code
---

## Getting Started

These instructions will get you a copy/replication of the project up and running on for testing purposes.  

### Assembly Instructions


### Step 1: Connect the Arduino to the DC Motor

Here's an image of the connected circuit:

![Circuit Image](/C04_solution/IMG_20250327_011913.jpg)

In this we can notice the entries used on the arduino for power in this case the 3v and 5v options and also the usage of the pins 9 for the enabling of the motor and also to control the speeds to which the DC motor would spin and the pins 1 and 2 to control the orientation of the rotation.

### Step 2: Connect the Arduino to the Raspberry Pi

Connect the Arduino to the Raspberry Pi via their USB ports.

### Step 3: Connect the Nicla Vision to the Raspberry Pi

Use a micro-USB to USB 3.0 cable to connect the Nicla Vision to an available USB port on the Raspberry Pi.

---

## Software Prerequisites

This section provides detailed instructions for installing the additional software required for the application to work on a Raspberry Pi 4 Model B (ARM-based).

### Install Python 3.11.2

If Python 3.11.2 is not already installed on your Raspberry Pi OS, use the following commands:

```sh
# Add the Deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa

# Update the package database
sudo apt update

# Install Python 3.11
sudo apt install python3.11
```


gotify
```
$ wget https://github.com/gotify/server/releases/download/v2.6.1/gotify-linux-arm64.zip

$ unzip gotify-linux-arm64.zip

$ chmod +x gotify-linux-arm64
```





### Installation

Follow these step-by-step instructions to build and run the application in the testing environment.

To install the raspberry pie OS follow the specific tutorial:

https://www.youtube.com/watch?v=jLff_K39qL4


### Step 2: Set Up the Arduino Code

1. Open the **Arduino IDE**.
2. Open the **motor control code**.
3. Connect the **Arduino** to your personal computer via **USB**.
4. Compile and **upload the code**.
5. Disconnect the **Arduino** from your PC and reconnect it to the **Raspberry Pi**.

---

### Step 3: Set Up the Camera

1. Connect the **Nicla Vision** to your PC.
2. Copy the following files to the camera:
   - **Object detection script** [code](/C04_solution/camera/Object_detection_send_data.py)
   - **Labels file** [code](/C04_solution/camera/labels.txt)
   - **Trained model** [code](/C04_solution/camera/trained.tflite)
3. Once copied, **disconnect** the camera from your PC and **connect it to the Raspberry Pi**.


## Connecting to the Raspberry Pi Over the Network  

Since the **Raspberry Pi** gets a **dynamic IP address** assigned by the host's internet connection (in this case, a colleague’s phone), follow these steps to find and connect to it.  

---

### Step 1: Find the Raspberry Pi's IP Address  

1. Connect your **computer** to the **same network** as the Raspberry Pi.  
2. Run the following command on your computer:  

  ```sh
   arp -a
  ```
3. The output will look something like this:

Interface: 192.168.234.179 --- 0x7
  Internet Address      Physical Address      Type
  192.168.234.238       96-06-0d-25-45-d2     dynamic
  192.168.234.255       ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static

Interface: 192.168.56.1 --- 0xb
  Internet Address      Physical Address      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 172.17.192.1 --- 0x4f
  Internet Address      Physical Address      Type
  172.17.205.231        00-15-5d-e1-cd-a5     dynamic
  172.17.207.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

4. Identify the Raspberry Pi’s IP address. It will always end in 219.

---

### Step 3.2: Connect to the Raspberry Pi via SSH  

Start each terminal by using, in case of the example provided the following on a personal computer connected to the 
cellphone internet hotspot:

```sh
ssh 192.168.234.219
```

Use **two terminal sessions**:  

#### **1. Start Gotify**  

```sh
sudo ./gotify-linux-arm64
```

#### **2. Start the Script**  

```sh
python3 script.py
```

The script will prompt for the **Gotify server IP**:  

```
Enter the IP address of the Gotify server:
```

Enter the **Raspberry Pi's IP address** (e.g., `192.168.234.219`).  

Then it is possible to see the camera processing its video capture and consequently its classification of the data also providing information when a notification is sent to the user connected to the raspberry:

```
Enter the IP address of the Gotify server: 192.168.234.219
Connected to OpenMV Cam on /dev/ttyACM0 and Arduino on /dev/ttyACM1 at 115200 baud.
Received from OpenMV: 0,100,0.56
Invalid data format received.
Received from OpenMV: x 100     y 140   score 0.66
Invalid data format received.
Received from OpenMV: plastic,100,140,0.66
Label: plastic, X: 100, Y: 140, Score: 0.66
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.61
Invalid data format received.
Received from OpenMV: plastic,100,140,0.61
Label: plastic, X: 100, Y: 140, Score: 0.61
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.58
Invalid data format received.
Received from OpenMV: paper,100,100,0.58
Label: paper, X: 100, Y: 100, Score: 0.58
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.65
Invalid data format received.
Received from OpenMV: plastic,100,140,0.65
Label: plastic, X: 100, Y: 140, Score: 0.65
Updated plastic count: 3
Received from OpenMV: x 100     y 100   score 0.61
Invalid data format received.
Received from OpenMV: paper,100,100,0.61
Label: paper, X: 100, Y: 100, Score: 0.61
Updated paper count: 3
Received from OpenMV: x 100     y 140   score 0.66
Invalid data format received.
Received from OpenMV: plastic,100,140,0.66
Label: plastic, X: 100, Y: 140, Score: 0.66
Updated plastic count: 4
plastic count reached 4. Sending to Arduino...
Sent to Arduino: plastic
Sent to OpenMV: ready
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.59
Invalid data format received.
Received from OpenMV: plastic,100,140,0.59
Label: plastic, X: 100, Y: 140, Score: 0.59
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.54
Invalid data format received.
Received from OpenMV: paper,100,100,0.54
Label: paper, X: 100, Y: 100, Score: 0.54
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.66
Invalid data format received.
Received from OpenMV: plastic,100,140,0.66
Label: plastic, X: 100, Y: 140, Score: 0.66
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 3
Received from OpenMV: x 100     y 140   score 0.55
Invalid data format received.
Received from OpenMV: plastic,100,140,0.55
Label: plastic, X: 100, Y: 140, Score: 0.55
Updated plastic count: 3
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Received from OpenMV: x 100     y 140   score 0.70
Invalid data format received.
Received from OpenMV: plastic,100,140,0.70
Label: plastic, X: 100, Y: 140, Score: 0.70
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.70
Invalid data format received.
Received from OpenMV: plastic,100,140,0.70
Label: plastic, X: 100, Y: 140, Score: 0.70
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.74
Invalid data format received.
Received from OpenMV: plastic,100,140,0.74
Label: plastic, X: 100, Y: 140, Score: 0.74
Updated plastic count: 3
Received from OpenMV: x 100     y 100   score 0.58
Invalid data format received.
Received from OpenMV: paper,100,100,0.58
Label: paper, X: 100, Y: 100, Score: 0.58
Updated paper count: 3
Received from OpenMV: x 100     y 140   score 0.55
Invalid data format received.
Received from OpenMV: plastic,100,140,0.55
Label: plastic, X: 100, Y: 140, Score: 0.55
Updated plastic count: 4
plastic count reached 4. Sending to Arduino...
Sent to Arduino: plastic
Sent to OpenMV: ready
Received from OpenMV: x 100     y 100   score 0.59
Invalid data format received.
Received from OpenMV: paper,100,100,0.59
Label: paper, X: 100, Y: 100, Score: 0.59
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.53
Invalid data format received.
Received from OpenMV: plastic,100,140,0.53
Label: plastic, X: 100, Y: 140, Score: 0.53
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.58
Invalid data format received.
Received from OpenMV: paper,100,100,0.58
Label: paper, X: 100, Y: 100, Score: 0.58
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.61
Invalid data format received.
Received from OpenMV: plastic,100,140,0.61
Label: plastic, X: 100, Y: 140, Score: 0.61
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 3
Received from OpenMV: x 100     y 100   score 0.59
Invalid data format received.
Received from OpenMV: paper,100,100,0.59
Label: paper, X: 100, Y: 100, Score: 0.59
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.55
Invalid data format received.
Received from OpenMV: plastic,100,140,0.55
Label: plastic, X: 100, Y: 140, Score: 0.55
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.61
Invalid data format received.
Received from OpenMV: plastic,100,140,0.61
Label: plastic, X: 100, Y: 140, Score: 0.61
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.50
Invalid data format received.
Received from OpenMV: paper,100,100,0.50
Label: paper, X: 100, Y: 100, Score: 0.50
Updated paper count: 3
Received from OpenMV: x 100     y 140   score 0.63
Invalid data format received.
Received from OpenMV: plastic,100,140,0.63
Label: plastic, X: 100, Y: 140, Score: 0.63
Updated plastic count: 3
Received from OpenMV: x 100     y 100   score 0.56
Invalid data format received.
Received from OpenMV: paper,100,100,0.56
Label: paper, X: 100, Y: 100, Score: 0.56
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Paper garbage bin is full! Sending notification...
Gotify notification sent successfully for paper bin!
Received from OpenMV: x 100     y 140   score 0.53
Invalid data format received.
Received from OpenMV: plastic,100,140,0.53
Label: plastic, X: 100, Y: 140, Score: 0.53
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.53
Invalid data format received.
Received from OpenMV: plastic,100,140,0.53
Label: plastic, X: 100, Y: 140, Score: 0.53
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.62
Invalid data format received.
Received from OpenMV: paper,100,100,0.62
Label: paper, X: 100, Y: 100, Score: 0.62
Updated paper count: 2
Received from OpenMV: x 100     y 100   score 0.55
Invalid data format received.
Received from OpenMV: paper,100,100,0.55
Label: paper, X: 100, Y: 100, Score: 0.55
Updated paper count: 3
Received from OpenMV: x 100     y 100   score 0.56
Invalid data format received.
Received from OpenMV: paper,100,100,0.56
Label: paper, X: 100, Y: 100, Score: 0.56
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 1
Received from OpenMV: x 100     y 100   score 0.56
Invalid data format received.
Received from OpenMV: paper,100,100,0.56
Label: paper, X: 100, Y: 100, Score: 0.56
Updated paper count: 2
Received from OpenMV: x 100     y 140   score 0.53
Invalid data format received.
Received from OpenMV: plastic,100,140,0.53
Label: plastic, X: 100, Y: 140, Score: 0.53
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.59
Invalid data format received.
Received from OpenMV: paper,100,100,0.59
Label: paper, X: 100, Y: 100, Score: 0.59
Updated paper count: 3
Received from OpenMV: x 100     y 140   score 0.51
Invalid data format received.
Received from OpenMV: plastic,100,140,0.51
Label: plastic, X: 100, Y: 140, Score: 0.51
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.57
Invalid data format received.
Received from OpenMV: paper,100,100,0.57
Label: paper, X: 100, Y: 100, Score: 0.57
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Received from OpenMV: x 100     y 140   score 0.73
Invalid data format received.
Received from OpenMV: plastic,100,140,0.73
Label: plastic, X: 100, Y: 140, Score: 0.73
Updated plastic count: 1
Received from OpenMV: x 100     y 100   score 0.58
Invalid data format received.
Received from OpenMV: paper,100,100,0.58
Label: paper, X: 100, Y: 100, Score: 0.58
Updated paper count: 1
Received from OpenMV: x 100     y 140   score 0.51
Invalid data format received.
Received from OpenMV: plastic,100,140,0.51
Label: plastic, X: 100, Y: 140, Score: 0.51
Updated plastic count: 2
Received from OpenMV: x 100     y 100   score 0.56
Invalid data format received.
Received from OpenMV: paper,100,100,0.56
Label: paper, X: 100, Y: 100, Score: 0.56
Updated paper count: 2
Received from OpenMV: x 100     y 100   score 0.58
Invalid data format received.
Received from OpenMV: paper,100,100,0.58
Label: paper, X: 100, Y: 100, Score: 0.58
Updated paper count: 3
Received from OpenMV: x 100     y 100   score 0.53
Invalid data format received.
Received from OpenMV: paper,100,100,0.53
Label: paper, X: 100, Y: 100, Score: 0.53
Updated paper count: 4
paper count reached 4. Sending to Arduino...
Sent to Arduino: paper
Sent to OpenMV: ready
Paper garbage bin is full! Sending notification...
Gotify notification sent successfully for paper bin!
```

In the other terminal where the gotify was called the output presented should be something of this kind

```

Starting Gotify version 2.6.1@2024-11-16-08:49:43
Started listening for plain connection on tcp [::]:80
2025-03-27T19:20:52Z | 200 |     267.246µs | 192.168.234.238 | GET      "/version"
2025-03-27T19:20:58Z | 200 |   205.69153ms | 192.168.234.238 | GET      "/current/user"
2025-03-27T19:21:02Z | 200 |   31.036515ms | 192.168.234.219 | POST     "/message?token=[masked]"
2025-03-27T19:21:03Z | 200 |  158.777585ms | 192.168.234.238 | POST     "/client"
2025-03-27T19:21:03Z | 200 |    8.596582ms | 192.168.234.238 | GET      "/current/user"
2025-03-27T19:21:03Z | 200 |      141.74µs | 192.168.234.238 | GET      "/version"
2025-03-27T19:21:03Z | 200 |     1.24966ms | 192.168.234.238 | GET      "/application"
2025-03-27T19:21:03Z | 200 |     714.814µs | 192.168.234.238 | GET      "/stream?token=[masked]"
2025-03-27T19:21:03Z | 200 |      4.0495ms | 192.168.234.238 | GET      "/message?limit=1&since=0"
2025-03-27T19:21:03Z | 200 |     831.625µs | 192.168.234.238 | GET      "/application"
2025-03-27T19:21:03Z | 200 |     912.136µs | 192.168.234.238 | GET      "/message?limit=100&since=0"
2025-03-27T19:21:03Z | 200 |   30.185383ms | 192.168.234.238 | GET      "/static/defaultapp.png"
2025-03-27T19:21:03Z | 200 |   30.275005ms | 192.168.234.238 | GET      "/static/defaultapp.png"
2025-03-27T19:21:05Z | 200 |    2.030306ms | 192.168.234.238 | GET      "/message?limit=100&since=0"
2025-03-27T19:21:05Z | 200 |     358.359µs | 192.168.234.238 | GET      "/static/defaultapp.png"
2025-03-27T19:21:27Z | 200 |   13.113875ms | 192.168.234.219 | POST     "/message?token=[masked]"
2025-03-27T19:21:27Z | 200 |     452.684µs | 192.168.234.238 | GET      "/static/defaultapp.png"
2025-03-27T19:21:35Z | 200 |    1.148315ms | 192.168.234.238 | GET      "/client"
2025-03-27T19:21:35Z | 200 |   10.436031ms | 192.168.234.238 | DELETE   "/client/21"

```


With this it is possible to verify that the project is fully functional

### Authors

* **Luís Filipe Pedro Marques** - *Setup Creator* - [PurpleBooth](https://github.com/Pacten15/)

* **Gustavo Manuel Cabral de Mascarenhas Diogo**  - *Hardware Designer and Report Writer* - [PurpleBooth](https://github.com/GMD433)

* **André Ferreira de Oliveira** - *Hardware Designer and Arduino setup* - [PurpleBooth](https://github.com/andre-foliveira256)

* **Jorge Cordeiro Hristovsky** - *Arduino setup and Report writer* - 

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

### Acknowledgments

* The edge impulse creators 
* The content creators that provided insight on how to setup the raspberry pie, to configure the arduino and many more techniques.