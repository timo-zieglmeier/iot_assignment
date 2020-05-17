# Start der Anwendung
import threading
import time
from config.config import Config
from alerts.alert_service import AlertService
from sensor.distance_sensor_thread import DistanceSensorThread as dst
from csv.logger_init import setup_logging, get_logger
from csv.csv_writer import CsvWriter

#Einlesen der brokerConfig.json
config = Config()
print(config.broker_host)

#Threads
iot_sensor_thread = dst("iot_sensor_thread")
#iot_mqtt_thread = myStartThread(2, "iot_mqtt_thread")

iot_sensor_thread.start()
#iot_mqtt_thread.start()
"""
#Logging
setup_logging()

get_logger(__name__).info('Test OK from main module')
writeToCSV = CsvWriter()
writeToCSV.write_line(iot_sensor_thread)
"""