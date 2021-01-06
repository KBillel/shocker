import serial
import time
import keyboard

def connect(COM):
    try:
        ser = serial.Serial(COM,9600,timeout=1)
        return ser
    except:
        return 0
def disconnect(ser):
    ser.close()
    
    
def load_protocol(path):
    protocol= []
    f = open(path,"r")
    
    for i in f:
        if (i[0] != "%") & (i[0] != "\n"):
            try:
                protocol.append([i.rstrip().split()[0], int(i.rstrip().split()[1])])
            except:
                return []
                
        else:
            continue
        
    return protocol
    
    
def shock(ser,t): 
    
    ser.write(b'S')
    ser.write(str(t).encode())
    a = time.time()
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()
    print(time.time()-a)
    print("Shock delivered")
    
def tone(ser,t):
    ser.write(b'T')
    ser.write(str(t).encode())
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()
    
    print("Tone delivered")
    
def shocktone(ser,t):
    ser.write(b'A')
    ser.write(str(t).encode())
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()

    print("ShockTone delivered")
    
def sleep(ser,t):
    ser.write(b'W')
    ser.write(str(t).encode())
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()
    print("Wait is done")
	
    
def start_exp(ser):
    ser.write(b'D')
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()
    print('Experiment Strated')
    
def end_exp(ser):
    ser.write(b'F')
    r = ser.readline().decode().rstrip()
    while r == "":
        r = ser.readline().decode().rstrip()
    print('Experiment Ended Succefully')
    