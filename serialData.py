import time
import serial
import httpRequest
import threading
import json

import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p.description)
ftdi_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'FT232R USB UART' in p.description  # may need tweaking to match new arduinos
]
if not ftdi_ports:
    raise IOError("found")
if len(ftdi_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(ftdi_ports[0],115200,timeout=1)

# configure the serial connections (the parameters differs on the device you are connecting to)
#ser =serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
#ser =serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

#http=httpRequest.Http()
class serialData:
    responseData=None
    flagResponse=False
    def __init__(self):
            
                    
        thread = threading.Thread(target=self.sync, args=())
        thread.daemon = True                            
        thread.start()

        self.initTxRx()
        time.sleep(5)
        self.conexion3g()


    def initTxRx(self):
        cmd1='\x03'
        ser.write(cmd1.encode())
        time.sleep(1)
        cmd1='\x04'
        ser.write(cmd1.encode())
        time.sleep(1)
        cmd1='\x12'
        ser.write(cmd1.encode())
        time.sleep(1)

    def conexion3g(self):
        x="CONNECT$-$-"
        x=x+'\x0D'
        ser.write(x.encode())
        

    def enviar(self,data):
        x=data+'\x0D'
        ser.write(x.encode())
        self.flagResponse=True
            
    
    def sync(self):
        js=None
        i=0
        while True:
            

            try:
                s=ser.readline()
                
                if len(s)>0:
                    
                    s.decode("utf-8")
                    data=str(s)
                    if data.startswith("b'{"):
                        self.responseData=data[2:len(data)-7]
                ser.flush()
            
            except Exception as e:
                print(e)

            time.sleep(0.01)

   

    


        
           

           
           
           
           



