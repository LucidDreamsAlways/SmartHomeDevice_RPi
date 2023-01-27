#configuring the code for the MQTT broker
#install mqtt if not done before
#sudo apt-get mosquitto
import paho.mqtt.client as mqtt
import time
    
mqtt_broker = "test.mosquitto.org"
topic = "smarthome/BME280/SummaryData"

my_mqtt = None


def onMessage(Client, userdata, message):
	print("%s %s" % (message.topic, message.summary_data))

def startMQTT():
	my_mqtt = mqtt.Client()
	my_mqtt.on_message = onMessage
	
	my_mqtt.connect(mqtt_broker, port=1883)
	my_mqtt.subscribe(topic, qos=1)
	my_mqtt.loop_start()
	print("Subscribed to Topic")

def main():
	startMQTT()
	while True:
		time.sleep(2)

if __name__ == "__main__":
	main()