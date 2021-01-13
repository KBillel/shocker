# Shocker

This repo contains codes used in the lab in order to control the fear conditioning cage.
All TTL sent by the arduino are also sent to digitalin on the Intan Board allowing for simple and easy synchronisation with ephys
## arduino
Contain the C code that you need to flash to the Arduino memory using the Arduino Software IDE

## Python
### shocker.py
Main code for the application. Run the GUI and modify it when necessary.
### arduino.py
Code used for interafacing with the arduino
### mainwindow.py
Code generated using PyQT5 UI code generator. Contains the design of the interface.
## requirments
requirments.txt file contain library used in the app. 
pip install requirements.txt 
