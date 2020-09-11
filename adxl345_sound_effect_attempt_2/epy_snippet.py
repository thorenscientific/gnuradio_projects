"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import adi

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
#Standard epy init stuff...
        self.example_param = example_param
        self.myacc=adi.adxl345(uri="local:")

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] =  input_items[0] * int(self.myacc.accel_z.raw)
        return len(output_items[0])

