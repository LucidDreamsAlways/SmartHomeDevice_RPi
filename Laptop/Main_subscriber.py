import paho.mqtt.client as mqtt

# List of topics to subscribe to
topics = ["smarthome/BME280/summary", "smarthome/BME280/temperature", "smarthome/BME280/humidity", "smarthome/BME280/pressure"]

# Callback function for when a message is received on a subscribed topic
def on_message(client, userdata, msg):
    print("Received message on topic: ", msg.topic)
    print("Message: ", msg.payload)

# Create an MQTT client
client = mqtt.Client()

# Set the callback function for when a message is received
client.on_message = on_message

# Connect to the MQTT broker
client.connect("172.20.10.12", 1883, 60)

# Subscribe to the topics in the list
for topic in topics:
    client.subscribe(topic)

# Start the client loop
client.loop_forever()
