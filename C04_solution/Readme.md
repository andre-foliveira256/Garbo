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
---

## Getting Started

These instructions will get you a copy/replication of the project up and running on for testing purposes.  

### Assembly Instructions

Describe step-by-step assembly instructions.

When necessary, and especially when wiring is involved, include diagrams/photos.

First it is needed to connect the arduino to the DC motor

Here's an image of the circuits connected:

![Circuit Image](/C04_solution/IMG_20250327_011913.jpg)


Then connect the arduino to the raspberry pie throw their usb ports 

Finally connect the nicla vision to the raspberry pie using a micro usb to usb 3.0 cable conneting to the raspberry to another free usb port.



### Software Prerequisites

In this section include detailed instructions for installing additiona software the application is dependent upon (such as PostgreSQL database, for example) being these necessary to make the project work on a raspberry pie 4 model B meaning it is arm based.

python 3.11.2
```
If not already installed on the raspberry pie operating system here's the commands

# Adding the Deadsnakes PPA
$ sudo add-apt-repository ppa:deadsnakes/ppa

# Updating the package database
$ sudo apt update

# Installing the Python 3.11
$ sudo apt install python3.11
```


gotify
```
$ wget https://github.com/gotify/server/releases/download/v2.6.1/gotify-linux-arm64.zip

$ unzip gotify-linux-arm64.zip

$ chmod +x gotify-linux-arm64
```





### Installation

Step-by-step instructions on building and running the application on the testing environment.

To install the raspberry pie OS follow the specific tutorial:

https://www.youtube.com/watch?v=jLff_K39qL4

To setup the code for the arduino start first to open the arduino IDE and then open the [code of the motor](/motor/motor.ino) then connect the arduino throw the usb to your personal computer and compile the code to the system with that done you just need to take the cable out and reconnect to the raspberry pie.

For the camera you connect it also to your personal computer and then copy the [detection code](/câmera/Object_detection_send_data.py)

Since this project depends on the host of the internet that is in our case one of the colleagues phones the ip changes randomly being that the raspberry pie also will have always a different ip so to start we need to first:

Connect the computer that is going to connect to the raspberry to the internet where the raspberry is connected to

Then do the following command on your computer:
```
arp -a
```
It will present as type of output like this one:

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

Then taking the information we have of this file we can connect to the raspberry pie using ssh being always his ip address ended on 219

So in this example we need to run two terminals using ssh.

Being one to start the gotify and another one to start the script

Assuming you unzip the gotify in the root
```
sudo ./gotify-linux-arm64

```

On the other terminal do the following 

1º Execute the script that will ask for the ip address of the machine in question being based on what was explained previously

```
python3 script.py
```

Should present this:

```
Enter the IP address of the Gotify server:
```

Being for the example presented the 192.168.234.219

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

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

### Versioning

We use [SemVer](http://semver.org/) for versioning. 
For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

### Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc