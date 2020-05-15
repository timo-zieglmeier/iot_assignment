from mqtt.mqtt_thread import MQTTThread as mqtt
from config.config import Config

class AlertService: # Service Reagiert auf Messwerte
    
    threshold = None
    #  Initialisierung
    def __init__(self, value):
        self.threshold = value

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold (self, value):
        self.threshold = value

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        if value < self.threshold:
            mqtt.client.connect("localhost", 1883)
            mqtt.client.publish(Config.alert_topic, "ACHTUNG!: Schwellwert unterschritten!")
        else:
            pass