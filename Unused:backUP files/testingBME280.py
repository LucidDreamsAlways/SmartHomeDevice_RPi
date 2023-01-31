import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)

print(f"Temperature: {data.temperature:.2f}°C")
print(f"Pressure: {data.pressure:.2f}hPa")
print(f"Humidity: {data.humidity:.2f}%")
