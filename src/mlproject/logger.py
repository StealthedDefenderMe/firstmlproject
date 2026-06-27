import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Filename with time and date
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #setting up the path of the log file
os.makedirs(log_path, exist_ok=True) #If folder is already available then skip

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Format of how my log message would work
    # time + line no + filename + levelname + message (error or success)
    level=logging.INFO #This is level could be warning and error as well
)