
#-*- coding:utf-8 -*-
import time
import datetime
import RPi.GPIO as GPIO
from alerts.alert_service import AlertService

class DistanceSensor:
    #  Initialisierung
    def __init__(self, sensorIDname='KY-050'):
        self.sensorID = sensorIDname
        

    #  return Wert als Dictionary 
    #  entsprechend folgendem JSON:
    #   { 
    #     "sensorId"  : "KY-050", 
    #     "timestamp" : "2020-03-01T12:00:01.345+01:00",
    #     "distance" : 42,
    #     "unit" : "cm"
    #   }


    def read_value(self):
        GPIO.setmode(GPIO.BCM)
        Trigger_AusgangsPin = 17
        Echo_EingangsPin    = 27

        GPIO.setup(Trigger_AusgangsPin, GPIO.OUT)
        GPIO.setup(Echo_EingangsPin, GPIO.IN)
        GPIO.output(Trigger_AusgangsPin, False)

        # Abstandsmessung wird mittels des 10us langen Triggersignals gestartet
        GPIO.output(Trigger_AusgangsPin, True)
        time.sleep(0.00001)
        GPIO.output(Trigger_AusgangsPin, False)
 
        # Hier wird die Stopuhr gestartet
        EinschaltZeit = time.time()
        while GPIO.input(Echo_EingangsPin) == 0:
            EinschaltZeit = time.time() # Es wird solange die aktuelle Zeit gespeichert, bis das Signal aktiviert wird
 
        while GPIO.input(Echo_EingangsPin) == 1:
            AusschaltZeit = time.time() # Es wird die letzte Zeit aufgenommen, wo noch das Signal aktiv war
 
        # Die Differenz der beiden Zeiten ergibt die gesuchte Dauer
        Dauer = AusschaltZeit - EinschaltZeit
        # Mittels dieser kann nun der Abstand auf Basis der Schallgeschwindigkeit der Abstand berechnet werden
        Abstand = (Dauer * 34300) / 2
 
        # Ueberpruefung, ob der gemessene Wert innerhalb der zulaessigen Entfernung liegt
        if Abstand < 2 or (round(Abstand) > 300):
            # Falls nicht wird eine Fehlermeldung ausgegeben
            print("Abstand außerhalb des Messbereich")
            print("------------------------------")
        else:
            # Der Abstand wird auf zwei Stellen hinterm Komma formatiert
            Abstand = float(format((Dauer * 34300) / 2, '.2f'))
            
            GPIO.cleanup()
            return {
                    "sensorID": self.sensorID,
                    "timestamp": datetime.datetime \
                    .fromtimestamp(time.time()).isoformat(),
                    "distance": Abstand,
                    "unit": "cm"
                    }
                
            

    