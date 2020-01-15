from time import sleep
from widgetlords.pi_spi import *
from widgetlords import *
import math
init()
inputs = Mod8AI()

class ReadCard:
    def readPort(self,numPort):
        val=0
        if numPort==0 :
            val=inputs.read_single(0)
            return val
        elif numPort==1:
            val=inputs.read_single(1)
            return val
        elif numPort==2:
            val=inputs.read_single(2)
            return val
        elif numPort==3:
            val=inputs.read_single(3)
            return val
        elif numPort==4:
            val=inputs.read_single(4)
            return val
        elif numPort==5:
            val=inputs.read_single(5)
            return val
        elif numPort==6:
            val=inputs.read_single(6)
            return val
        elif numPort==7:
            val=inputs.read_single(7)
            return val
    
    def readInputVoltaje(self,numInput):
        adcMax=4095
        vRef=6.6
        value=self.readPort(numInput)
        voltaje=(vRef*value)/adcMax
        return voltaje
    
    def readInputCorriente(self,numInput):
        adcMax=3723
        mA=20
        resolucion=20/3723
        value=self.readPort(numInput)
        corriente=value*resolucion
        return corriente

    def valorInstrumentacion(self,data):
        sen=data[0]
        ri_min=data[1]
        ri_max=data[2]
        rp_min=data[3]
        rp_max=data[4]
        try:
            x=self.readInputCorriente(sen)
            
            
            rangoInstrumentacion=ri_max-ri_min
            rangoProceso=rp_max-rp_min
            rirp=rangoInstrumentacion/rangoProceso
            val=((ri_max-x)/rirp)-rp_max
            val=val*-1
            return val
            
        except Exception as e:
            return 0
    
    def sensorHumeda(self,data):
        sen=data[0]
        ri_min=data[1]
        ri_max=data[2]
        rp_min=data[3]
        rp_max=data[4]
        try:
            x=self.readInputVoltaje(sen)
            rangoInstrumentacion=ri_max-ri_min
            rangoProceso=rp_max-rp_min
            rirp=rangoInstrumentacion/rangoProceso
            val=((ri_max-x)/rirp)-rp_max
            val=val*-1
            val=math.floor(val)
            return val
        except Exception as e:
            return 0
         






        