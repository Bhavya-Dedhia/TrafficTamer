## Prerequisites
Before starting, ensure you are on a Linux system (like Ubuntu or Debian) and have Python 3 installed.

### Step 1: Install Dependencies
Run the commands given in Commands file to set up everything required for TrafficTamer.

### Step 2: Create Your Project Directory
This is where all your files will live.

### Step 3: Create the Main Python File
You'll now create the app file that runs the TrafficTamer GUI.
##### Open nano editor to create your GUI script
```nano app_gui.py```<br>
Then, paste the full Python GUI code into the file (make sure the class is properly indented and all __init__, if __name__ == "__main__": blocks are correct).
<br>
Once pasted, save and exit:
- Press Ctrl + O to save
- Press Enter to confirm the filename
- Press Ctrl + X to exit nano

### Step 4: Run TrafficTamer
Since TrafficTamer uses Linux's tc (traffic control), it must be run as root:<br>
```sudo python3 app_gui.py```<br>
You should now see the GUI window appear showing real-time upload/download graph. Use the buttons to:
- Apply Traffic Shaping (limit bandwidth)
- Clear Shaping
- Reset Graph
- Save Graph as Image

### Step 5: Check Traffic Shaping Rules
Open a new terminal window and run:<br>
```sudo tc -s qdisc show dev enp0s3```<br>
- This shows current traffic shaping (qdisc) rules on the interface enp0s3.
- Change enp0s3 to your actual network interface if needed. Use ip a to find your active one.


#### That's it!
You're now fully set up to use TrafficTamer for visualizing and controlling your Linux network bandwidth.
