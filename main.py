
import smbus2, bme280, json

# BME280 sensor Initialization (comment below 3 lines to use simulated data)
address = 0x77
bus = smbus2.SMBus(1) 
calibration_params = bme280.load_calibration_params(bus, address)


def temp_pub():
    
    while True:
        
        data = bme280.sample(bus, address, calibration_params)
        temp = round(data.temperature, 2)
        
        #Update current time - from epoch seconds to IST
        timestamp = int(time.time())
        ist_offset = 5.5 * 3600
        ist_time = time.localtime(timestamp + ist_offset)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', ist_time)

        sensor_data = {
            "sensorData": [
                {
                    "timestamp": formatted_time,
                    "temperature": temp
                }
            ]
        }
        
        message = json.dumps(sensor_data)
        print(f"Published: {message}")
        
        # Wait for 60 seconds before next reading
        time.sleep(1)

if __name__ == "__main__":
    temp_pub()
