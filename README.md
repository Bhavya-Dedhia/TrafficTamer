# TrafficTamer

A network traffic shaping and monitoring tool with a graphical user interface (GUI). It monitors real-time upload and download speeds on a specified network interface, displays this data on a live graph, and lets you apply or clear traffic shaping rules (rate limiting)

It helps users to visualize their network traffic and control bandwidth on a network interface easily through a GUI.
It is useful for testing, network management, or throttling bandwidth for specific interfaces.


## Key features:
- Real-time network speed monitoring (upload/download)
- Graphical display of network speeds using PyQt5 and pyqtgraph
- Buttons to apply bandwidth limits (traffic shaping), clear them, reset the graph, and save the graph as an image
- Works on Linux with root privileges to apply traffic control (tc)
