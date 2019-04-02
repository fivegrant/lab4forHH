#/usr/bin/python3
# Five and Zak

from smbus import *

class Circuit:
    def __init__(self, bus, adc, backpack):
        self.bus = bus
        self.adc = adc
        self.backpack = backpack
        self.vout = 0

    def write_block(self, device_address, 
     cmd, parameters):
        if device_address == 'backpack':
            self.bus.write_i2c_block_data(self.backpack, \
             cmd, parameters)
        else:
            self.bus.write_i2c_block_data(self.adc, \
             cmd, parameters)

    def write_byte(self, cmd):
        self.bus.write_byte(self.backpack, cmd)

    def update(self, temp):
        cells = [0b0, 0b10, 0b110, 0b1000]
        num = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111, 0]
        if temp == 'clear':
            for cell in cells:
                self.write_block('backpack', cell, [0])
        else:
            temp = str(temp)
            while len(temp) < 4:
                temp = ' ' + temp
            iter = 0
            for char in temp:
                retrieve = 10
                try: 
                   retrieve = int(char) 
                except:
                    pass
                self.write_block('backpack', cells[iter], [num[retrieve]])
                iter += 1

    def get_raw_adc_reading(self, conversionr):
        raw_reading = self.bus.read_i2c_block_data(
         self.adc, conversionr)
        msb = raw_reading[0] << 8
        return msb + raw_reading[1]

    def convert_raw_reading(self, conversionr, rang):
        self.vout = self.get_raw_adc_reading(conversionr) * (rang/32767)
        return self.vout   

    def convert_voltage_to_temp(self, r2, vin):
        r1 = ((vin*r2)/self.vout) - r2
        m, b = (-0.001565, 51.11)
        return r1 * m + b

