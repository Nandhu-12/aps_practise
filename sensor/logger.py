import logging
import datetime
import os,sys

'''
create log_file_name
create log_dir
makesure log_dir if not exists create one
create log_file_path
do log basicconfiguration
'''

log_file_name = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
log_dir = os.path.join(os.getcwd(),"logs")
os.makedirs(log_dir,exist_ok = True)
log_file_path = os.path.join(log_dir,log_file_name)

logging.basicConfig(
    filename = log_file_path,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,)