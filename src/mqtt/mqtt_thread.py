import paho.mqtt.client as mqtt
import time
import threading

class MQTTThread(threading.Thread):
    def __init__(self):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

    def on_connect(client, userdata, flags, rc):
        print("Verbunden mit Result Code "+str(rc))
        client.subscribe("$Sys/#")

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    #client = mqtt.Client()
    #client.on_connect = on_connect
    #client.on_message = on_message