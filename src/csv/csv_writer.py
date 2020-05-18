import logging

class CsvWriter:
    distance = None

    #  Initialisierung
    def __init__(self, distance):
        self.distance = distance

    #  line: ist die bereits formatierte Zeile, die nur noch geschrieben wird.
    def write_line (self):
        logging.info("Gemessene Distanz in cm: ")
        logging.info(self.distance)