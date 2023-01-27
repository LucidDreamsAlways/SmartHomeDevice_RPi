import threading
import SensorData

if __name__ == "__main__":
    sensor_thread = threading.Thread(target=SensorData.main)
    sensor_thread.start()


import subprocess

# start the sensorData.py script as a separate process
sensor_process = subprocess.Popen("python sensorData.py", shell=True)

# your main script code here

# when you are ready to stop the sensorData.py process
sensor_process.terminate()
