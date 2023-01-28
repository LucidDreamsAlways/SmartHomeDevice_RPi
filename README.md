# IOT-Project
 Smart Home Device
 
 The first file(SensorData.py) of code is written for a Raspberry Pi and is responsible for collecting environmental data using a BME280 sensor, which measures temperature, humidity, and pressure. It also controls a fan and a buzzer based on the temperature readings. Once the data is collected, it is published to an MQTT broker, which acts as a middleman, forwarding the data to other devices that are connected to the network.

The second file(writesmarthomeDB.py) of code is written for a laptop and is responsible for subscribing to the MQTT topics that the Raspberry Pi is publishing the data to. Once the data is received, it is then stored in an InfluxDB database, which is a time-series database that is optimized for storing and querying large quantities of time-stamped data. This allows for easy retrieval and analysis of the collected data, providing a convenient way to monitor the environment. Together, these two files of code work in harmony to create a monitoring device that can collect and store environmental data, making it possible to keep track of changes in temperature, humidity, and pressure in real-time.

In addition to using the Python script to collect and process the data, we can also store the data in InfluxDB, a time-series database. This will allow us to easily query and analyze the data over time. We can then use Grafana, a popular open-source dashboard tool, to visualize the data stored in InfluxDB.


![alt text](https://github.com/LucidDreamsAlways/IOT-Project/blob/main/ProjectDesign.png?raw=true)
