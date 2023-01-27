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




#configuring the code for the MQTT broker
#install mqtt if not done before
#sudo apt-get mosquitto
import paho.mqtt.client as mqtt
import time

mqtt_broker = "172.20.10.12"  # replace with the IP address of your laptop
topic = "smarthome/BME280/SummaryData"

while True:
    # Summary data
    summary_data = AllData_BME280  # assuming this variable contains the string you want to publish

    # Create a new client object
    my_mqtt = mqtt.Client()
    print("\nCreated client object at "+ time.strftime("%H:%M:%S"))

    # Connect to the broker
    my_mqtt.connect(mqtt_broker, port=1883)  # assuming you're using the default MQTT port
    print("--connected to broker")

    try:
        # Publish the data to the broker
        my_mqtt.publish(topic, summary_data)
        print("--BME280 data summary = " + str(summary_data))

    except:
        # Print an error message if the data is not published
        print("--error publishing!")

    else:
        # Disconnect from the broker and print a message
        my_mqtt.disconnect()
        print("--disconnected from broker")

    # Add a delay before the next iteration
    time.sleep(60)



        
'''
import argparse
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import time
import random

USER = 'root'
PASSWORD = 'root'
DBNAME = 'mydb'
HOST = 'localhost'
PORT = 8086
dbclient = None;

def main():
    dbclient = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)
    while True:
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
            time.sleep(2)

            
return(pointValues)
    if __name__ == '__main__':
    main()
    Main.py
'''
