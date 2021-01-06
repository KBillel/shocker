# Shocker_3000
# Billel KHOUADER
# Version : 0.1
# Date 24/06/2020

# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
import time
import csv
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog

from mainwindow import Ui_MainWindow
import arduino

class gui:


    protocol = []
    save_list = []
    username = ""
    ser = 0
    t_start = 0

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Connect
        self.ui.connect_button.clicked.connect(self.connect)
        self.ui.load_button.clicked.connect(self.get_protocole_file)
        self.ui.username_button.clicked.connect(self.get_username)
        self.ui.start_button.clicked.connect(self.start_experiment)
        self.ui.save_button.clicked.connect(self.save_experiment)
        
    def show(self):
        self.main_win.show()
    
    
    # Action post button pressings.
    def connect(self):
        if self.ser == 0:
            self.COM = self.ui.COM_box.currentText()
            self.ser = arduino.connect(self.COM)
            if self.ser == 0:
                print('error')
                self.ser = []
            else:
                self.ui.arduino_status.setText("Arduino connect on port : "+self.COM)
        else:
            try:
                self.ser.close()
            except:
                print("Could not close Serial")
            
            self.COM = self.ui.COM_box.currentText()
            self.ser = arduino.connect(self.COM)
            if self.ser == 0:
                print('error')
            else:
                self.ui.arduino_status.setText("Arduino connect on port : "+self.COM)
            
            
    
        
    def get_protocole_file(self):
        fileName = QFileDialog.getOpenFileName(self.main_win,"Open Protocole File", "C://Users//billel.khouader//Documents//Shocker_3000", "Protocole Files (*.prtcl)")
        protocol_path = fileName[0]
        self.protocol = arduino.load_protocol(protocol_path)
        
        if self.protocol != []:
            self.ui.protocol_path.setText(fileName[0])
            self.ui.protocol_status.setText("Protocol Loaded")
        else:
            self.ui.protocol_status.setText("Wrong File Format")
        
    def get_username(self):
        self.username = self.ui.username.text()
        
    
    def start_experiment(self):
        self.save_list = []
        self.t_start = datetime.now().strftime("%Y%d%m") 
        if self.protocol == []:
            self.ui.protocol_status.setText("Protocol Not Loaded")
            return 0
        if self.ser == []:
            self.ui.arduino_status.setText("Arduino not connected")
            return 0
        
        self.ui.experiment_status.setText("Experiment running")
        
        
        time.sleep(0.5)
        
        arduino.start_exp(self.ser)
        
        for i in self.protocol:
            d = time.time()
            if i[0] == "SHOCK":
                print("SHOCK for "+str(i[1]))
                self.save_list.append([datetime.now().strftime("%H:%M:%S.%f"),"SHOCK"])
                arduino.shock(self.ser, i[1])
                
            elif i[0] == "TONE":
                print("TONE for "+str(i[1]))
                self.save_list.append([datetime.now().strftime("%H:%M:%S.%f"),"TONE"])
                arduino.tone(self.ser, i[1])
                
            elif i[0] == "SHOCKTONE":
                print("BOTH for "+str(i[1]))
                self.save_list.append([datetime.now().strftime("%H:%M:%S.%f"),"SHOCKTONE"])
                arduino.shocktone(self.ser, i[1])
                
            elif i[0] == "SLEEP":
                print("SLEEP for "+str(i[1]))
                self.save_list.append([datetime.now().strftime("%H:%M:%S:%f"),"SLEEP"])
                arduino.sleep(self.ser, i[1])
                
        self.ui.experiment_status.setText("Experiment done")
        arduino.end_exp(self.ser)

    def save_experiment(self):
        print(self.save_list)

        with open(self.username+self.t_start+".csv", mode='w',newline="") as save_file:
            save_writer = csv.writer(save_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            save_writer.writerows(self.save_list)

app = QApplication([])
window = gui()
window.show()
sys.exit(app.exec_())
