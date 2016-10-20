import logging

logging.basicConfig(filename='06_example_log.log', level=logging.INFO, format='[%(asctime)s] %(name)-12s %(levelname)s: %(message)s')
logging.info("start")
logging.info("one thing done.")
logging.info("another thing done.")
logging.info("all finished.")
