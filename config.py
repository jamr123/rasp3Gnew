#Ubidots Log
"""
UBIDOTS_TOKEN = 'BBFF-HHmBlj5C4CVgIrlBjgakdtyeFsYx1p' 
UBIDOTS_API_KEY='BBFF-7bacbcf068b323745bbdb16423f195797bb'
UBIDOTS_NAME_DEVICE ='Pozos 1 y 2 Belen' 
"""

UBIDOTS_TOKEN = 'BBFF-IH5I4OcjNkdFY6IAcKjnBhbdEThV8j' 
UBIDOTS_API_KEY='BBFF-e95568780d8217c718fac68bf30c60c2c30'
UBIDOTS_NAME_DEVICE ='POZOS_1_Y_2_BELEN' 

URI_CREAR_TOKEN='https://industrial.api.ubidots.com/api/v1.6/auth/token/'
URI_DEVICE='https://industrial.api.ubidots.com/api/v1.6/devices/'

#Variables Ubidots
UBIDOTS_SENSOR_A1='nivel1'
UBIDOTS_SENSOR_A2='nivel2'
UBIDOTS_SENSOR_A3='presion1'
UBIDOTS_SENSOR_A4='presion2'
UBIDOTS_SENSOR_A5='sensor5'
UBIDOTS_SENSOR_A6='sensor6'
UBIDOTS_SENSOR_A7='sensor7'
UBIDOTS_SENSOR_CAUDAL_1='caudal1'
UBIDOTS_SENSOR_CAUDAL_2='caudal2'
UBIDOTS_SENSOR_HUMEDAD_1='humedad1'
UBIDOTS_SENSOR_HUMEDAD_2='humedad2'
UBIDOTS_SENSOR_TEMPERATURA_1='temperatura1'
UBIDOTS_MOTOR_1_SWITCH_REMOTO='interruptorRemoto1'
UBIDOTS_MOTOR_2_SWITCH_REMOTO='interruptorRemoto2'
UBIDOTS_MOTOR_1_HORAS='motor1horas'
UBIDOTS_MOTOR_2_HORAS='motor2horas'
#Configuraciones de Sensores

LCD_ADDRESS=0x3f

PROFUNDIDAD_SENSOR_NIVEL1=50#rango de medida
PROFUNDIDAD_SENSOR_NIVEL2=50#rango de medida

PROFUNDIDAD_POZO_1=54#profundidad de instalacion
PROFUNDIDAD_POZO_2=54#profundidad de instalacion

ADJN1=0
ADJN2=0

SENSOR_PRESION_1=10
SENSOR_PRESION_2=10

S1=[0,4,20,0,PROFUNDIDAD_SENSOR_NIVEL1] #nivel1
S2=[1,4,20,0,PROFUNDIDAD_SENSOR_NIVEL2] #nivel2
S3=[2,4,20,0,SENSOR_PRESION_1] #presion1
S4=[3,4,20,0,SENSOR_PRESION_2] #presion2
S5=[4,0,20,0,100] #sensor5
S6=[5,0,20,0,100] #sensor6
S7=[6,0,20,0,100] #sensor7
S8=[7,1.75,0.5,0,100]#Humedad suelo


#Configuraciones REPORTES
REPORT_TIMER = 60  #Segundos
#Configuracion sensores CAUDAL
CAUDAL_SENSOR_1_GPIO = 25 #GPIO     
CAUDAL_SENSOR_1_PULSOS = 100     #Pulsos X Litro
CAUDAL_SENSOR_2_GPIO = 9 #GPIO        
CAUDAL_SENSOR_2_PULSOS = 100     #Pulsos X Litro
#Configuracion MOTORES
MOTOR_SWITCH_1_GPIO = 17  
MOTOR_RELAY_1_GPIO  = 24
MOTOR_SWITCH_2_GPIO  = 18
MOTOR_RELAY_2_GPIO  = 4    

#Configuraciones sensor dht22
DHT22_GPIO = 23 #GPIO 
#Config LCD
#ADDRESS_LCD=0 #i2c 3(SDA) y 5(SCL)

UBIDOTS_VAR_NAMES = [

                    UBIDOTS_SENSOR_A1,
                    UBIDOTS_SENSOR_A2,
                    UBIDOTS_SENSOR_A3,
                    UBIDOTS_SENSOR_A4,
                    UBIDOTS_SENSOR_A5,
                    UBIDOTS_SENSOR_A6,
                    UBIDOTS_SENSOR_A7,
                    UBIDOTS_SENSOR_CAUDAL_1,
                    UBIDOTS_SENSOR_CAUDAL_2,
                    UBIDOTS_MOTOR_1_SWITCH_REMOTO,
                    UBIDOTS_MOTOR_2_SWITCH_REMOTO,
                    UBIDOTS_SENSOR_HUMEDAD_1,
                    UBIDOTS_SENSOR_HUMEDAD_2,
                    UBIDOTS_SENSOR_TEMPERATURA_1,
                    UBIDOTS_MOTOR_1_HORAS,
                    UBIDOTS_MOTOR_2_HORAS
                    ]


HTTP_CREATE_TOKEN='https://industrial.api.ubidots.com/api/v1.6/auth/token/'
HTTP_GET_DATASOURSE='https://industrial.api.ubidots.com/api/v1.6/datasources/'
HTTP_CREATE_DEVICE='https://industrial.api.ubidots.com/api/v1.6/devices/'
HTTP_VALUE='https://industrial.api.ubidots.com/api/v1.6/devices/'
HTTP_GET_DEVICE='https://industrial.api.ubidots.com/api/v1.6/devices/'


