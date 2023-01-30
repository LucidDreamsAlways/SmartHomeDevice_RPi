import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

# MQTT connection details
MQTT_BROKER = "172.20.10.12"
MQTT_PORT = 1883
MQTT_TOPICS = ["smarthome/BME280/temperature", "smarthome/BME280/humidity", "smarthome/BME280/pressure", "smarthome/fan/status", "smarthome/fan/control"]

# InfluxDB connection details
INFLUXDB_HOST = "localhost"
INFLUXDB_PORT = 8086
INFLUXDB_USER = "root"
INFLUXDB_PASSWORD = "root"
INFLUXDB_DBNAME = "smarthome_db"

# Initialize InfluxDB client
dbclient = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASSWORD, INFLUXDB_DBNAME)

# MQTT callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

    # Subscribe to all topics in MQTT_TOPICS
    for topic in MQTT_TOPICS:
        client.subscribe(topic)

# MQTT callback for when a message is received on one of the subscribed topics
def on_message(client, userdata, msg):
    print("Received message on topic " + msg.topic + ": " + str(msg.payload))
    payload = msg.payload.decode("utf-8") # decode the payload from bytes to string
    measurement = msg.topic.split("/")[-1]
    try:
        # Try to convert the payload to a float
        value = float(payload)
    except ValueError:
        # If it fails, assume the payload is a string
        value = payload
    data_point = [
        {
            "measurement": measurement,
            "fields": {"value": value}
        }
    ]
    #Save data into InfluxDB
    dbclient.write_points(data_point)

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Main loop
client.loop_forever()

