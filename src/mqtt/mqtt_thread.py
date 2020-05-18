import paho.mqtt.client as mqtt
from config.config import Config
import time
import threading

class MQTTThread(threading.Thread):
    def __init__(self, name, out_queue, in_queue):
        threading.Thread.__init__(self)
        self.name = name
        self.out_queue = out_queue
        self.in_queue = in_queue

    def on_connect(client, userdata, flags, rc):
        print("Verbunden mit Result Code "+str(rc))
        client.subscribe("$Sys/#")

    def on_message(client, userdata, msg):
        #print(msg.topic+" "+str(msg.payload))
        if message.topic == Config.config_topic:
            client.pub("distance_sensor/config",int(message.payload.decode()))

    client = mqtt.Client()
    config = Config()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(config.broker_host, config.broker_port)
    #client.subscribe("distance_sensor/config", AlertService.set_alert_threshold)
    
    