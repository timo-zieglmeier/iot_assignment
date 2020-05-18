import threading
import time
import logging
from sensor.distance_sensor import DistanceSensor
from alerts.alert_service import AlertService
from csv.csv_writer import CsvWriter

class DistanceSensorThread(threading.Thread):
    def __init__(self, name, out_queue, in_queue):
        threading.Thread.__init__(self)
        self.name = name
        self.out_queue = out_queue
        self.in_queue = in_queue

    def run(self):
        sleeptime = 2.0
        distanceToAlert = AlertService(20)
        
        

        while True:
            print("Starte Thread ",self.name)
            getDistance = DistanceSensor()
            distance = getDistance.read_value()
            print(distance)
            distanceToAlert.on_distance_threshold_passed(distance["distance"])

            self.out_queue.put(distance)
            if not self.in_queue.empty():
                new_threshold = self.in_queue.get()

            #Logging
            tocsv = CsvWriter(distance["distance"])
            tocsv.write_line()

            time.sleep(sleeptime)