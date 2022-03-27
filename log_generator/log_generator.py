import logging
import sys

logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    stream=sys.stdout,
    level=logging.DEBUG,
    )

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger().addHandler(console)

logger = logging.getLogger(__name__)

import time
import math

i = 0
while True:
    logger.info(math.sin(math.pi/10000*i))
    time.sleep(0.001)
    i+=1