import sys
import psutil
import time
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyqtgraph as pg

INTERFACE = "enp0s3"  # <- Your active interface

class NetworkMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Shaping & Monitoring Tool")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Monitoring network traffic...", self)

        # Buttons
        self.button_shape = QPushButton("Apply Traffic Shaping", self)
        self.button_clear = QPushButton("Clear Shaping", self)
        self.button_reset = QPushButton("Reset Graph", self)
        self.button_save = QPushButton("Save Graph", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.button_shape)
        btn_layout.addWidget(self.button_clear)
        btn_layout.addWidget(self.button_reset)
        btn_layout.addWidget(self.button_save)
        layout.addLayout(btn_layout)

        # Graph setup
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setTitle("Real-time Upload/Download Speed")
        self.plot_widget.setLabel('left', 'Speed', units='KB/s')
        self.plot_widget.setLabel('bottom', 'Time', units='s')
        self.plot_widget.addLegend()

        self.download_line = self.plot_widget.plot(pen='y', name="Download")
        self.upload_line = self.plot_widget.plot(pen='r', name="Upload")

        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

        # Button actions
        self.button_shape.clicked.connect(self.apply_shaping)
        self.button_clear.clicked.connect(self.clear_shaping)
        self.button_reset.clicked.connect(self.reset_graph)
        self.button_save.clicked.connect(self.save_graph)

        # Data
        self.max_points = 60
        self.x_data = list(range(self.max_points))
        self.download_data = [0] * self.max_points
        self.upload_data = [0] * self.max_points

        self.old_sent, self.old_recv = self.get_bytes()

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def get_bytes(self):
        counters = psutil.net_io_counters(pernic=True)
        if INTERFACE in counters:
            return counters[INTERFACE].bytes_sent, counters[INTERFACE].bytes_recv
        return 0, 0

    def update_stats(self):
        sent_now, recv_now = self.get_bytes()
        sent_rate = (sent_now - self.old_sent) / 1024
        recv_rate = (recv_now - self.old_recv) / 1024

        self.label.setText(f"Upload: {sent_rate:.2f} KB/s | Download: {recv_rate:.2f} KB/s")

        self.upload_data = self.upload_data[1:] + [sent_rate]
        self.download_data = self.download_data[1:] + [recv_rate]

        self.upload_line.setData(self.x_data, self.upload_data)
        self.download_line.setData(self.x_data, self.download_data)

        self.old_sent, self.old_recv = sent_now, recv_now

    def apply_shaping(self):
        subprocess.call(f"sudo tc qdisc add dev {INTERFACE} root tbf rate 1mbit burst 32kbit latency 400ms", shell=True)

    def clear_shaping(self):
        subprocess.call(f"sudo tc qdisc del dev {INTERFACE} root", shell=True)

    def reset_graph(self):
        self.upload_data = [0] * self.max_points
        self.download_data = [0] * self.max_points

    def save_graph(self):
        exporter = pg.exporters.ImageExporter(self.plot_widget.plotItem)
        exporter.export("traffic_graph.png")
        QMessageBox.information(self, "Saved", "Graph saved as traffic_graph.png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NetworkMonitor()
    win.show()
    sys.exit(app.exec_())
