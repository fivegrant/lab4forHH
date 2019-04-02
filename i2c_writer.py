#/usr/bin/python3
# Five and Zak

from smbus import *

class Circuit:
    def __init__(self, bus, adc, backpack, row_cmd):
        self.bus = bus
        self.adc = adc
        self.backpack = backpack
        self.row_cmd = row_cmd
        self.vout = 0

    def write_block(self, device_address, 
     cmd, parameters):
        if device_address == 'backpack':
            self.bus.write_i2c_block_data(self.backpack, \
             cmd, parameters)
        else:
            self.bus.write_i2c_block_data(self.adc, \
             cmd, parameters)

    def write_byte(self, device_address, cmd):
        if device_address == 'backpack':
            self.bus.write_byte(self.backpack, cmd)
        else: 
            self.bus.write_byte(self.adc, cmd)

    def light(self, which):
        self.write_byte('backpack', rowint_cmd+which)
            
    def get_raw_adc_reading(self, conversionr):
        raw_reading = self.bus.read_i2c_block_data(
         self.adc, conversionr)
        msb = raw_reading[0] << 8
        return msb + raw_reading[1]

    def convert_raw_reading(self, rang):
        self.reading = self.get_raw_adc_reading(conversionr)* (rang/32767)
        return self.reading    

    def convert_voltage_to_temp(self, r2, vin):
        r1 = ((vin*r2)/self.vout) - r2
        m, b = (-0.001565, 51.11)
        return r1 * m + b

