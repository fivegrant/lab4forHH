#!/usr/bin/python3
# Five and Zak

from smbus import *

device_address = 0x70


def tell_backback(my_bus, 
 address, command, parameters):
    my_bus.write_i2c_block_data(device_address,\
     config_register, config_bytes)

def shove_backpack(my_bus, command):
    my_bus.write_byte(device_address, command)

