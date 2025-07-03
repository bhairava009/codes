import logging

logging.basicConfig(filename="app.log")
level = logging.INFO,format ="%(acetime)s -%(levelname)s -%(message)s"
logging.info("program started")

try:
    x=10/0
