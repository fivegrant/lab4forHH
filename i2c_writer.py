#/usr/bin/python3
# Five and Zak

from smbus import *

def write_register(my_bus, device_address, 
 config_register, conversion_register, config_bytes):
    my_bus.write_i2c_block_data(device_address,\
     config_register, config_bytes)

def write_byte(my_bus, device_address, command):
    my_bus.write_byte(device_address, command)
   
def get_raw_adc_reading(my_bus):
    raw_reading = my_bus.read_i2c_block_data(\
     da, conversionr)
    msb = raw_reading[0] << 8
    return msb + raw_reading[1]

def convert_raw_reading(raw_reading, rang):
    return raw_reading * (rang/32767)
    
def convert_voltage_to_temp(vout, r2, vin):
    r1 = ((vin*r2)/vout)-r2
    m, b = (-0.001565, 51.11)
    return r1 * m + b

