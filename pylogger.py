from datetime import datetime

class Logger():
    
    # Constants used to pass in event types
    ERROR = "Error"
    DATA_SCRAPE = "Data Scrape"
    DATA_PERSIST = "Data Inserted Into DB"

    def __init__(self, app_name, logfile_dst=None):
        if logfile_dst is None:
            logfile = app_name + "_log.txt"
        else:
            logfile = logfile_dst + app_name + "_log.txt"


    def log(self, event_type, message):
        log_string = str(datetime.now()) + "\t" + event_type + "\t" + message
        with open(self.logfile, 'a+') as f:
            f.write(log_string)