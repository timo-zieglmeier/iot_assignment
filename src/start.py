# Start der Anwendung
import threading
import time
import logging
from queue import Queue
from mqtt.mqtt_thread import MQTTThread
from config.config import Config
from alerts.alert_service import AlertService
from sensor.distance_sensor_thread import DistanceSensorThread as dst
from csv.csv_writer import CsvWriter

logging.basicConfig(filename="log.csv", format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG)

#Einlesen der brokerConfig.json
config = Config()
print(config.broker_host)

#Threads
sensor_out_queue = Queue()
sensor_in_queue = Queue()

iot_sensor_thread = dst("iot_sensor_thread", sensor_out_queue, sensor_in_queue)
iot_mqtt_thread = MQTTThread("iot_mqtt_thread", sensor_in_queue, sensor_out_queue)

iot_sensor_thread.start()
iot_mqtt_thread.start()
"""
#Logging
setup_logging()

get_logger(__name__).info('Test OK from main module')
writeToCSV = CsvWriter()
writeToCSV.write_line(iot_sensor_thread)
"""