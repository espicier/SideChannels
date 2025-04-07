import numpy as np
import chipwhisperer as cw

# Sources used
# https://github.com/coastalwhite/cw-rsa
# http://wiki.newae.com/Making_Scripts#XMEGA_Target
# https://chipwhisperer.readthedocs.io/en/latest/Targets/CW303%20XMEGA.html (Not used yet)

# Setup our capture and target boards.
########################################
scope = cw.scope()
#scope.default_setup()

scope.gain.gain = 45
scope.adc.samples = 5000
scope.adc.offset = 0
scope.adc.basic_mode = "rising_edge"
scope.clock.clkgen_freq = 7370000
scope.clock.adc_src = "clkgen_x4"
scope.trigger.triggers = "tio4"
scope.io.tio1 = "serial_rx"
scope.io.tio2 = "serial_tx"

target = cw.target(scope, cw.targets.SimpleSerial2, flush_on_err=False)
########################################

# Reprogram the target
########################################
import os
#from chipwhisperer.capture.api.programmers import STM32FProgrammer
from chipwhisperer.capture.api.programmers import XMEGAProgrammer

"""
PLATFORM = 'CWLITEXMEGA'

try:
    if not scope.connectStatus:
        scope.con()
except NameError:
    scope = cw.scope()

try:
    target = cw.target(scope)
except IOError:
    print("INFO: Caught exception on reconnecting to target - attempting to reconnect to scope first.")
    print("INFO: This is a work-around when USB has died without Python knowing. Ignore errors above this line.")
    scope = cw.scope()
    target = cw.target(scope)

print("INFO: Found ChipWhisperer😍")

if "STM" in PLATFORM or PLATFORM == "CWLITEARM" or PLATFORM == "CWNANO":
    prog = cw.programmers.STM32FProgrammer
elif PLATFORM == "CW303" or PLATFORM == "CWLITEXMEGA":
    prog = cw.programmers.XMEGAProgrammer
else:
    prog = None
"""

"""
# Initiate a new STM32F Program
# STM32 being the ARM microcontroller that we are using
# https://en.wikipedia.org/wiki/STM32#STM32_F3
program = STM32FProgrammer
"""
program = XMEGAProgrammer
program.scope = scope

# Get the path to the current folder
# Adjust accordingly
aes_firmware_dir = os.path.dirname(os.path.realpath(__file__))
aes_hex_path = os.path.join(aes_firmware_dir, r"outputs/rsa_spa/rsa_spa-CWLITEXMEGA.hex")

# Apply the program to the actual target
# This allows us to run the hex code on the microcontroller
cw.program_target(scope, program, aes_hex_path)
########################################

# Capture a trace of our binary
########################################
# Define some dummy data
data = bytearray([0x42] * 16)

# Arm the capture board
scope.arm()

# Flush the UART buffer
target.flush()

# Send a new command to trigger our code.
# Here we use scmd = 128
target.send_cmd('p', 0x80, data)

# Do our wave trace capture
# and fetch that wave trace
ret = scope.capture()
trace = scope.get_last_trace()
########################################

# Return the data.
########################################
# Print the returned data
returned_data = target.read_cmd('r')
print(returned_data)
ack = target.read_cmd('e')

import matplotlib.pyplot as plt

# Plot the trace
plt.plot(trace)
plt.show()
########################################
