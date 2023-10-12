import os
import sys
import logging

# logging message format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Dir to Save Log Files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  # Save log to file
        logging.StreamHandler(sys.stdout)  # print log on terminal also
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
