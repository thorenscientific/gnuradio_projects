"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import random


#import sys
import zmq

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='0MQ_RX_adxl345',   # will show up in GRC
            in_sig=[np.single],
            out_sig=[np.single, np.single, np.single]
            
        )

        self.xst = 0
        self.yst = 0
        self.zst = 0
        random.seed()
#        print("version: " + sys.version)
        port = "5556"

        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket = context.socket(zmq.SUB)
        self.socket.connect ("tcp://localhost:%s" % port)
        topicfilter = "10001"
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

#    def work(self, input_items, output_items):
    def work(self, input_items, output_items):
        """Scale input with acceleration values, send to 3 outputs"""
        try:
            self.st = self.socket.recv(flags=zmq.NOBLOCK) # If nothing published, move on
            print("got string...:" + str(self.st))
            topic, self.xst, self.yst, self.zst = self.st.split()
#            self.xst = random.randint(-256, 256)
#            self.yst = random.randint(-256, 256)
#            self.zst = random.randint(-256, 256)

        except:
            pass
        
        output_items[0][:] = input_items[0] * (float(self.xst)+256.0) # add offset to keep positive
        output_items[1][:] = input_items[0] * (float(self.yst)+256.0)
        output_items[2][:] = input_items[0] * (float(self.zst)+256.0)
        return len(output_items[0])
