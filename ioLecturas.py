import RPi.GPIO as GPIO
import readCard
import sys
import config
import connUbidotsHttp
import threading
from threading import Timer
import math
import socket
import time





ubi=connUbidotsHttp.Ubidots()
readConvert=readCard.ReadCard()



class Data:
    estadoSw1=False
    estadoSw2=False
    countCaudal1=0
    countCaudal2=0
    lcdCount=0
    hm1=0
    hm2=0
    sm1=0
    sm2=0

    
    

    def __init__(self):
          
        
        
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.CAUDAL_SENSOR_1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(config.CAUDAL_SENSOR_1_GPIO, GPIO.BOTH, callback=self.ISR_caudal_1, bouncetime=1500)
        
        GPIO.setup(config.CAUDAL_SENSOR_2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(config.CAUDAL_SENSOR_2_GPIO, GPIO.BOTH, callback=self.ISR_caudal_2, bouncetime=1500)
        
        thread = threading.Thread(target=self.calculoCaudales, args=())
        thread.daemon = True                            
        thread.start()


    def cleanUp(self):
        try:
            GPIO.cleanup()
            ubi.threadCancel()
        except Exception as e:
            print(e)
        return 

    
        
                

    def leerTarjeta(self):

        n1=config.PROFUNDIDAD_POZO_1-readConvert.valorInstrumentacion(config.S1)
        n2=config.PROFUNDIDAD_POZO_2-readConvert.valorInstrumentacion(config.S2)
        n1=n1-config.ADJN1
        n2=n2+config.ADJN2
        print(n1)
        print(n2)

        
        p1=readConvert.valorInstrumentacion(config.S3)
        p2=readConvert.valorInstrumentacion(config.S4)

        ubi.lecturas[config.UBIDOTS_SENSOR_A1]=float("{0:.2f}".format(n1))
        ubi.lecturas[config.UBIDOTS_SENSOR_A2]=float("{0:.2f}".format(n2))
        ubi.lecturas[config.UBIDOTS_SENSOR_A3]=float("{0:.2f}".format(p1))
        ubi.lecturas[config.UBIDOTS_SENSOR_A4]=float("{0:.2f}".format(p2))
        
        print(ubi.lecturas[config.UBIDOTS_SENSOR_A3])
        print(ubi.lecturas[config.UBIDOTS_SENSOR_A4])
        
        
    def crearReporte(self):
        self.leerTarjeta()
        

    def ISR_caudal_1(self,channel):
        self.countCaudal1=self.countCaudal1 + 1 
        print("sr1")
        print(self.countCaudal1)
        
        

    def ISR_caudal_2(self,channel):
        self.countCaudal2=self.countCaudal2 + 1
        print("sr2")
        print(self.countCaudal2) 
        
    
        
    def calculoCaudales(self):
        while True:
            print("calculo caudales")
            pulsos=self.countCaudal2
            litros=pulsos*config.CAUDAL_SENSOR_2_PULSOS
            caudal=litros/60
            ubi.lecturas[config.UBIDOTS_SENSOR_CAUDAL_2]=float("{0:.2f}".format(caudal))
            self.countCaudal2=0

            pulsos=self.countCaudal1
            litros=pulsos*config.CAUDAL_SENSOR_1_PULSOS
            caudal=litros/60
            ubi.lecturas[config.UBIDOTS_SENSOR_CAUDAL_1]=float("{0:.2f}".format(caudal))
            self.countCaudal1=0


            time.sleep(60)




    
    

    
        
            

    
   
        
