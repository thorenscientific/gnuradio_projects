"""
Read ADXL345 raw values, publish to topic 10001, localhost
"""

import zmq
import sys
import time
import adi

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

myacc = adi.adxl345(uri="ip:localhost")
myacc.sampling_frequency = 100.0


while True:
    topic = 10001
    x = myacc.accel_x.raw
    y = myacc.accel_y.raw
    z = myacc.accel_z.raw
    print("%d %d %d %d" % (topic, x, y, z))
    socket.send_string("%d %d %d %d" % (topic, x, y, z))
    time.sleep(0.4)