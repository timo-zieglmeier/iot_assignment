from csv.logger_init import get_logger


class CsvWriter:

    #  Initialisierung
    def __init__(self):
        pass

    #  line: ist die bereits formatierte Zeile, die nur noch geschrieben wird.
    def write_line (self, line):
         logger = get_logger(__name__)
         logger.info(f'{line}')