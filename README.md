# TrafficTamer

A network traffic shaping and monitoring tool with a graphical user interface (GUI). It monitors real-time upload and download speeds on a specified network interface, displays this data on a live graph, and lets you apply or clear traffic shaping rules (rate limiting)

TrafficTamer is a lightweight Linux desktop application designed to monitor, visualize, and control network bandwidth in real-time. With an intuitive graphical user interface (GUI), it empowers users to apply traffic shaping rules and observe their effects instantly.


## Key features:
- Real-time network speed monitoring (upload/download)
- Graphical display of network speeds using PyQt5 and pyqtgraph
- Buttons to apply bandwidth limits (traffic shaping), clear them, reset the graph, and save the graph as an image
- Works on Linux with root privileges to apply traffic control (tc)

## System Requirements
**OS:** Linux (Ubuntu/Debian or compatible)<br>
**Python:** 3.6 or higher<br>
**Privileges:** Root access (for applying tc shaping)<br>
**Packages:**
- psutil
- pyqtgraph
- PyQt5
- tc (usually included in iproute2 package)

## Installation & Setup
All detailed instructions are given in **"Full Setup Guide" & "Commands"** file

## Screenshots
![Screenshot 2025-06-12 222523](https://github.com/user-attachments/assets/caa97773-75bf-4ee7-9a6d-b10601c6f860)

#### TrafficTamer – Upload and Download speeds Graph
![Screenshot 2025-06-12 223525](https://github.com/user-attachments/assets/9ee5bd8b-87a0-4358-b74e-c98c6d694596)

##### TrafficTamer – After applying traffic shaping 
![Screenshot 2025-06-12 222609](https://github.com/user-attachments/assets/f1d99ee4-adc5-4819-9b9d-c1c6e4569774)

TrafficTamer – After clear traffic shaping
![Screenshot 2025-06-12 222714](https://github.com/user-attachments/assets/a52d0cdc-d317-46aa-93b1-73b531b9900b)

TrafficTamer – Reset
![Screenshot 2025-06-12 222828](https://github.com/user-attachments/assets/b7c1d876-75dc-4a74-af8d-617d850c8c4a)

TrafficTamer – Check Shaping
![Screenshot 2025-06-12 222925](https://github.com/user-attachments/assets/ed1d3a7c-1713-4b47-9160-1c2c2b69745d)


## Usage
- Apply Traffic Shaping: Limit upload/download speed.
- Clear Shaping: Remove all bandwidth limits.
- Reset Graph: Clear current data and restart graphing.
- Save Graph: Export current graph view as an image (.png).
