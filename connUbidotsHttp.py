import config
from ubidots import ApiClient
import threading
import logging
import time
import math
import serialData
import json

ser=serialData.serialData()

class Ubidots:
    token=None
    stop_threads =False
    api = None
    datasource = None
    device=None
    variables=None
    valueVariables=None
    listaVariables=[]
    varConnect=False
    transmision=False
    
    lecturas={
        config.UBIDOTS_SENSOR_A1:0,
        config.UBIDOTS_SENSOR_A2:0,
        config.UBIDOTS_SENSOR_A3:0,
        config.UBIDOTS_SENSOR_A4:0,
        config.UBIDOTS_SENSOR_A5:0,
        config.UBIDOTS_SENSOR_A6:0,
        config.UBIDOTS_SENSOR_A7:0,
        config.UBIDOTS_SENSOR_CAUDAL_1:0,
        config.UBIDOTS_SENSOR_CAUDAL_2:0,
        config.UBIDOTS_SENSOR_HUMEDAD_1:0,
        config.UBIDOTS_SENSOR_HUMEDAD_2:0,
        config.UBIDOTS_SENSOR_TEMPERATURA_1:0,
    }
    botones={
        config.UBIDOTS_MOTOR_1_SWITCH_REMOTO:0,
        config.UBIDOTS_MOTOR_2_SWITCH_REMOTO:0
    }
    horas={
         config.UBIDOTS_MOTOR_1_HORAS:0,
         config.UBIDOTS_MOTOR_2_HORAS:0
    }
    

    def __init__(self):
        try:
            time.sleep(10)
            self.auth()                                
            self.deviceFind()
            self.configVariables()
            self.stop_threads =False
            thread = threading.Thread(target=self.sync, args=())
            thread.daemon = True                            
            thread.start()

        except Exception as e:
            print(e)

    
    def threadCancel(self):
        self.stop_threads =True

        
    def auth(self):
        data='TOKEN$'+config.HTTP_CREATE_TOKEN+'$'+config.UBIDOTS_API_KEY
        tk=self.readSerial(data)
        self.token=tk['token']
        
        
    def deviceFind(self):
        dev=json.dumps({"":""})
        data='POST$https://industrial.api.ubidots.com/api/v1.6/devices/'+config.UBIDOTS_NAME_DEVICE+'/$'+self.token+'$'+dev
        ds=self.readSerial(data)
        self.variables = 0

    def configVariables(self):
        for dato in config.UBIDOTS_VAR_NAMES:
                self.lecturas[dato]=self.getVariable(dato)
                time.sleep(1)

        
    def actualizarVal(self, varName, value):
        
            data =json.dumps( {"value": value,"timestamp": math.trunc(time.time())*1000})

            try:
               
                url=config.HTTP_VALUE+config.UBIDOTS_NAME_DEVICE+'/'+varName+'/values/'
                data2='POST$'+url+'$'+self.token +'$'+data
                ds2=self.readSerial(data2)
                return ds2
            except Exception as e:
                print(e)    
        
    def getVariable(self,varName):
        
        try:
            
            url=config.HTTP_VALUE+config.UBIDOTS_NAME_DEVICE+'/'+varName
            data2='GET$'+url+'$'+self.token
            ds2=self.readSerial(data2)
            ds1=ds2['last_value']
            ds=ds1['value']
            return ds
        except Exception as e:
            print(e)

    def readSerial(self,data):
        ser.enviar(data)
        i=0
        d=None
        js=None
        while d==None:
            i=i+1
            d=ser.responseData
            time.sleep(0.01)

        ser.responseData=None
        try:
            js=json.loads(d)
            return js
        except Exception as e:
            return {"":""}

    
    def sync(self):
        while True: 
            
            self.transmision=True
            for dato in self.lecturas:
                self.actualizarVal(dato,self.lecturas[dato])
                time.sleep(1)
            
            self.transmision=False
            print(self.lecturas)
            time.sleep(config.REPORT_TIMER)     
            

    def btns(self):
        while True:
            if self.transmision==False:
                try:
                    self.botones[config.UBIDOTS_MOTOR_1_SWITCH_REMOTO]=self.getVariable(config.UBIDOTS_MOTOR_1_SWITCH_REMOTO) 
                    time.sleep(3)
                    self.botones[config.UBIDOTS_MOTOR_2_SWITCH_REMOTO]=self.getVariable(config.UBIDOTS_MOTOR_2_SWITCH_REMOTO) 
                except Exception as e:
                    self.actualizarVal(config.UBIDOTS_MOTOR_1_SWITCH_REMOTO,0)
                    self.actualizarVal(config.UBIDOTS_MOTOR_2_SWITCH_REMOTO,0)

                    print(e)
            time.sleep(10)

    
        



