#This is the main file that the smart home program will run on.

from gpiozero import LED
fan = LED(17)

buzzer = LED(18)

#Configuring the code for BME280
#importing the required libs for using the BME280
import bme280
import smbus2
from time import sleep

#configuring to collect data via the BME280
port = 1
address = 0x76 #This is the port use on pypi.org/project/RPi.bme280 but note that this is not the same chip we have, similar tho...
bus = smbus2.SMBus(port)

#calibration parameters for BME280
bme280.load_calibration_params(bus,address)

#Start loop
BME280_status = 1 #Value set at 1 for ON and 0 for OFF, this determines if the BME280 is using the sensors.

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    #Creating a  summary value for sending the data to the MQTT broker.
    #This can be used to present all data during testing too :))
    AllData_BME280 = ("\nThe humidity = " + str(humidity) + "\nThe Air Pressure = " + str(pressure) + "\nThe temperature = " + str(ambient_temperature))
    print(AllData_BME280)

    #Make the BME280 chip delay by 1sec
    sleep(1)



    if ambient_temperature > 28.5:
        fan.on()
        buzzer.on()

    else:
        fan.off()
        buzzer.off()
        print("zzz")


'''
while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    #Creating a  summary value for sending the data to the MQTT broker.
    #This can be used to present all data during testing too :))
    AllData_BME280 = ("\nThe humidity = " + str(humidity) + "\nThe Air Pressure = " + str(pressure) + "\nThe temperature = " + str(ambient_temperature))
    print(AllData_BME280)

    #Make the BME280 chip delay by 1sec
    sleep(1)

    if ambient_temperature > 30:
        fan.on()
        sleep(3)
        fan.off()
        sleep(3)
    else:
        print("zzz")
'''

#configuring the code for the MQTT broker
#install mqtt if not done before
#sudo apt-get mosquitto
import paho.mqtt.client as mqtt
    
mqtt_broker = "test.mosquitto.org"
topic = "smarthome/BME280/SummaryData"

while True:
    #Client is created
    my_mqtt = mqtt.Client()
    print("\nCreated client object at "+ time.strftime("%H:%M:%S"))
    #MQTT is now connected to port 1883, note that this is not a secure port. We will use port 8883 for a more secure connecion.
    my_mqtt.connect(mqtt_broker, port=1883)
    print("--connected to broker")

    try:
        #Publishing the data to the MQTT broker, Topic is named BME280/SummaryData
        my_mqtt.publish(topic, AllData_BME280)
        print("--BME280 data summary = " % AllData_BME280)
    
    except:
        #To print error if the data is not published
        print("--error publishing!")
    
    else:
        #to print the message if the device disconnected from the mqtt broker
        my_mqtt.disconnect()
        print("--disconnected from broker")



