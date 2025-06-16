# TrafficTamer

A network traffic shaping and monitoring tool with a graphical user interface (GUI). It monitors real-time upload and download speeds on a specified network interface, displays this data on a live graph, and lets you apply or clear traffic shaping rules (rate limiting)

TrafficTamer is a lightweight Linux desktop application designed to monitor, visualize, and control network bandwidth in real-time. With an intuitive graphical user interface (GUI), it empowers users to apply traffic shaping rules and observe their effects instantly.


## Key features:
- Real-time network speed monitoring (upload/download)
- Graphical display of network speeds using PyQt5 and pyqtgraph
- Buttons to apply bandwidth limits (traffic shaping), clear them, reset the graph, and save the graph as an image
- Works on Linux with root privileges to apply traffic control (tc)

## System Requirements
**OS:** Linux (Ubuntu/Debian or compatible)
**Python:** 3.6 or higher
**Privileges:** Root access (for applying tc shaping)
**Packages:**
- psutil
- pyqtgraph
- PyQt5
- tc (usually included in iproute2 package)

## Installation & Setup
All detailed instructions are given in **"Full Setup Guide" & "Commands"** file

## Screenshots

## Usage
- Apply Traffic Shaping: Limit upload/download speed.
- Clear Shaping: Remove all bandwidth limits.
- Reset Graph: Clear current data and restart graphing.
- Save Graph: Export current graph view as an image (.png).
