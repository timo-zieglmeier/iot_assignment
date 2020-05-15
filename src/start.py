# Start der Anwendung
import threading
import time
from config.config import Config
from alerts.alert_service import AlertService
from sensor.distance_sensor_thread import DistanceSensorThread as dst

#Einlesen der brokerConfig.json
config = Config()
print(config.broker_host)

#Threads
iot_sensor_thread = dst("iot_sensor_thread")
#iot_mqtt_thread = myStartThread(2, "iot_mqtt_thread")

iot_sensor_thread.start()
#iot_mqtt_thread.start()