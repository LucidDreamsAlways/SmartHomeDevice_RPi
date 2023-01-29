import bme280
import smbus2
import time
import paho.mqtt.client as mqtt
from gpiozero import LED

#Assign piGPIO pins for fan and buzzer
fan = LED(17)
buzzer = LED(18)
fanStatus = 0
fanControl = 0

# BME280 sensor configuration
port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)

# MQTT broker configuration
mqtt_broker = "172.20.10.12"
#topicSummary = "smarthome/BME280/summary"
topicTemp = "smarthome/BME280/temperature"
topicHumid = "smarthome/BME280/humidity"
topicPressure = "smarthome/BME280/pressure"
topicFanStatus = "smarthome/fan/status"
topicFanControl = "smarthome/fan/control"

# Callback function for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Callback function for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    if msg.topic == topicFanControl:
        global fanControl
        fanControl = int(msg.payload)
    print(msg.topic + " " + str(msg.payload))


# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, 1883)
client.loop_start()

while True:
    # Collect data from the BME280 sensor
    bme280_data = bme280.sample(bus, address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    if fanControl == 1:
        fan.on()
        fanStatus = 1
    else:
        if ambient_temperature > 28.5:
            fan.on()
            fanStatus = 1
            buzzer.on()
        else:
            fan.off()
            buzzer.off()
            fanStatus = 0
            print("fan is not on")


    # Create a summary of the data
    summary_data = ("\nThe humidity = " + str(humidity) + "\nThe Air Pressure = " + str(pressure) + "\nThe temperature = " + str(ambient_temperature))
    print(summary_data)
    
    # Publish the temperature data to the broker
    client.publish(topicTemp, ambient_temperature)
    client.publish(topicHumid, humidity)
    client.publish(topicPressure, pressure)
    #client.publish(topicSummary, summary_data)
    client.publish(topicFanStatus, fanStatus)
    client.publish(topicFanControl, fanControl)
    
    # Delay for 2 seconds
    time.sleep(2)
