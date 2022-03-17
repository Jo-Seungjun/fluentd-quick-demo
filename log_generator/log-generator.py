import logging
import sys

logging.basicConfig(
    format='%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
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
    
for x in range(1, 10000):    
    logger.info(math.sin(math.pi/10000*x*10))
    time.sleep(0.001)