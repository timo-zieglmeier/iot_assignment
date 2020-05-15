import json
import os

class Config:
    broker_host = None
    broker_port = None
    config_topic = None
    data_topic = None
    alert_topic = None

    def __init__(self, file='brokerConfig.json'):
        file = os.path.join(os.path.dirname(__file__), file)
        with open(file) as f:
            config = json.load(f)

        Config.broker_host     =   config["broker_host"]
        Config.broker_port     =   config["broker_port"]
        Config.config_topic    =   config["config_topic"]
        Config.data_topic      =   config["data_topic"]
        Config.alert_topic     =   config["alert_topic"]

