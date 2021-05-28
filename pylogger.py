from datetime import datetime
import os

class Logger():
    
    # Constants used to pass in event types
    ERROR = "ERROR"
    DATA_SCRAPE = "DATA_SCRAPE"
    DATA_PERSIST = "DATA_PERSIST"
    LOGFILESTART = "LOGFILESTART"
    

    def __init__(self, app_name, logfile_dst=None):
        if logfile_dst is None:
            self.logfile = app_name + "_log.txt"
        else:
            self.logfile = logfile_dst + app_name + "_log.txt"

        if(os.path.isfile(self.logfile)):
            pass
        else:
            self.log(self.LOGFILESTART, "Logfile created")



    def log(self, event_type, message):
        log_string = str(datetime.now()) + "\t" + event_type + "\t" + message
        with open(self.logfile, 'a+') as f:
            f.write(log_string)