import pylogger

def main():
    logger = pylogger.Logger("Logger")
    logger.log(logger.TEST, "Testing logfile")

if __name__ == "__main__":
    main()