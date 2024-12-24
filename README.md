# Read BME280 on linux device

## Overview

This project involves setting up a Raspberry Pi running Ubuntu Server 20.04 with a BME280 sensor to print data.


## Repository Structure

```
.
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

Ensure you have Python 3.6+ installed on both the Raspberry Pi and the subscriber machine. Use the `requirements.txt` file to install necessary dependencies.

## Setup Instructions

### Step 1: Set Up the Python Environment

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/hippyaki/linux-python-bme280.git
   cd linux-python-bme280
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Step 2: Raspberry Pi Configuration

1. **Connect the BME280 sensor** to the Raspberry Pi.
2. **Run the script** on the Raspberry Pi:
   ```sh
   python main.py
   ```

## Program Descriptions


This script runs on the Raspberry Pi and prints sensor data from the BME280. Ensure that the required modules specified in the `requirements.txt` file are installed before running this script.


## Conclusion

Follow these steps to set up the environment, run the scripts, and access the sensor data. Ensure all dependencies are installed as per the `requirements.txt` file. This setup enables you to collect, store, and retrieve sensor data efficiently.

For any issues or queries, feel free to contact me at [akshayan.sinha@gmail.com].
