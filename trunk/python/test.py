#!usr/bin/env python

import logging, os

fName, fTail = __file__.split(".")
fLogName = "/Users/fernando/FRE/FRES/trunk/notes/" +fName+".log"
logging.basicConfig(level=logging.DEBUG, 		# Set the logging level
					format=' %(asctime)s - %(levelname)s - %(message)s', 
					datefmt="%H:%M:%S", # %Y-%m-%d %H:%M:%S or a, %d %b %Y %H:%M:%S
					filename=fLogName, 
					filemode="w")

logging.debug("This is a debug message (root level).")
logging.info("This is a info message. (2nd level)")
logging.warning("This is a warning message (3rd level).")
logging.error("This is an error message (4th level).")
logging.critical("This is a critical message (top level).")
