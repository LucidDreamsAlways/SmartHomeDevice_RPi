import paho.mqtt.client as mqtt
import time

# Callback function for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Publish a message to the topic "test/topic"
    client.publish("test/topic", "Hello from Raspberry Pi!")

# Callback function for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("172.20.10.12", 1883)

while True:
    # Publish a message to the topic "test/topic"
    client.publish("test/topic", "Hello from Raspberry Pi!")
    # Delay for 2 seconds
    time.sleep(2)
    # Process network events
    client.loop()
