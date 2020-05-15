import threading
import time
from sensor.distance_sensor import DistanceSensor
from alerts.alert_service import AlertService

class DistanceSensorThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleeptime = 2.0
        distanceToAlert = AlertService(20)
        
        while True:
            print("Starte Thread ",self.name)
            getDistance = DistanceSensor()
            distance = getDistance.read_value()
            print(distance)
            
            distanceToAlert.on_distance_threshold_passed(distance["distance"])

            time.sleep(sleeptime)