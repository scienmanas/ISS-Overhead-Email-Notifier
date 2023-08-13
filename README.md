# ISS Tracker and Daylight Alert System

This Python script tracks the International Space Station (ISS) in real-time and alerts you via email when the ISS is near your location during nighttime hours. It uses the ISS API to fetch the current position of the ISS and the Sunrise-Sunset API to determine the sunrise and sunset times for your specified location.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your machine.
- The `requests` library, which can be installed using `pip`:
```bash
pip install requests
```
- An active internet connection to fetch data from APIs.
- A valid email account for sending alerts

## Getting Started
1. Clone this repository to your local machine using:
```bash
git clone https://github.com/scienmanas/ISS-Overhead-Email-Notifier
```
2. Navigate to the project directory:
```bash
cd ISS-Overhead-Email-Notifier
```
3. Open the main.py file and update the MY_LAT and MY_LONG variables with your desired latitude and longitude. These coordinates will determine your location for the ISS tracking and daylight alerts.

4. Run the script using the following command:
```bash
python3 main.py
```

## How It Works
The script fetches the current position of the ISS using the ISS API. It then retrieves sunrise and sunset times for your specified location using the Sunrise-Sunset API. The script continuously monitors the time and ISS position. If the current time is during nighttime (after sunset and before sunrise) and the ISS is within a 5-degree range of your specified location, an email alert is sent using the configured email account.

## Customization
Feel free to customize the script according to your needs. You can adjust the sleep interval (currently set to 60 seconds) to control how often the script checks for the ISS position and time. Additionally, you can modify the email content, subject, and recipients to match your preferences.

## Disclaimer
This script is provided as-is and may require adjustments based on your specific use case and environment. Use it responsibly and ensure that you comply with the terms of use of the APIs and email services you are using.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
