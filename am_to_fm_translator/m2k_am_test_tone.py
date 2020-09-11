#
# Copyright (c) 2019 Analog Devices Inc.
#
# This file is part of libm2k
# (see http://www.github.com/analogdevicesinc/libm2k).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

# This example assumes the following connections:
# W1 -> 1+
# W2 -> 2+
# GND -> 1-
# GND -> 2-
#
# The application will generate a sine and triangular wave on W1 and W2. The signal is fed back into the analog input
# and the voltage values are displayed on the screen

import libm2k
import matplotlib.pyplot as plt
import time
import numpy as np

ctx=libm2k.m2kOpen("ip:192.168.3.1")
if ctx is None:
    print("Connection Error: No ADALM2000 device available/connected to your PC.")
    exit(1)

#ctx.calibrateADC()
ctx.calibrateDAC()

#ain=ctx.getAnalogIn()
aout=ctx.getAnalogOut()
#trig=ain.getTrigger()

#ain.enableChannel(0,True)
#ain.enableChannel(1,True)
#ain.setSampleRate(100000)
#ain.setRange(0,-10,10)

### uncomment the following block to enable triggering
#trig.setAnalogSource(0) # Channel 0 as source
#trig.setAnalogCondition(0,libm2k.RISING_EDGE_ANALOG)
#trig.setAnalogLevel(0,0.5)  # Set trigger level at 0.5
#trig.setAnalogDelay(0) # Trigger is centered
#trig.setAnalogMode(1, libm2k.ANALOG)

aout.setSampleRate(0, 7500000) #7.5Msps, adequate for 1MHz carrier
aout.setSampleRate(1, 7500000)
aout.enableChannel(0, True)
aout.enableChannel(1, True)



t=np.linspace(0.0,0.01,75000) #75ks over 10ms
buffer2=np.linspace(-2.0,2.00,75000)
#buffer1=np.sin(t)
buffer1=(2*(1+(0.4*(np.cos(600*2*np.pi*t)+np.cos(500*2*np.pi*t))))*np.sin(1000000*2*np.pi*t))

buffer = [buffer1, buffer2]
print("Pushing data...")
aout.setCyclic(True)
aout.push(buffer)

# for i in range(10): # gets 10 triggered samples then quits
#     data = ain.getSamples(1000)
plt.plot(buffer1)
plt.show()
time.sleep(0.1)
input("press any key to exit...")
print("bye!")
libm2k.contextClose(ctx)
