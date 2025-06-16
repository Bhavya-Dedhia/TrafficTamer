## Essential Setup Commands for TrafficTamer

1. **Update Package List**
<br>```sudo apt update```<br>
This command updates your system’s list of available packages and their versions.<br>
Also ensures you are installing the latest and compatible versions of dependencies like PyQt5 and system tools.

2. **Install Python Libraries**
<br>```pip3 install psutil pyqtgraph```<br>
psutil: Used by TrafficTamer to access live network stats (bytes sent/received).<br>
pyqtgraph: Allows you to draw the real-time network speed graph inside the GUI.

3. **Install PyQt5 (System Package)** <br>
```sudo apt install python3-pyqt5```<br>
This command installs the PyQt5 GUI framework system-wide.<br>
Also enables the creation of the application's graphical interface (windows, buttons, layouts).

4. **Redundant (but Safe) PyQt5 Install via pip** <br>
```sudo python3 -m pip install PyQt5```<br>
In case your system package doesn’t work properly, this ensures that PyQt5 is available in your Python environment.<br>
Often needed on minimal or custom Linux installs.

5. **Reinstall pyqtgraph (just in case)** <br>
```sudo python3 -m pip install pyqtgraph```<br>
This command ensures pyqtgraph is installed in the correct environment if pip3 install didn’t place it properly.<br>
TrafficTamer relies on it for live graph rendering.

6. **Clean Up the Cache** <br>
```sudo python3 -m pip cache purge```<br>
This command clears pip’s downloaded package cache.<br>
It frees up disk space and ensures a fresh environment in case you reinstall or debug any module issues.
<br>

#### These commands make sure your system is ready to run TrafficTamer smoothly by installing:

**PyQt5** → GUI toolkit<br>
**pyqtgraph** → real-time graphing<br>
**psutil** → network monitoring backend<br>
<br>
Each one is essential for a stable and visually responsive experience with your app.
