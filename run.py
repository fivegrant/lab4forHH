#/usr/bin/python3
from i2c_writer import *
import sys, time

#ADC
adc_address = 0x48
configr= 0x01
conversionr= 0x00
cb = [0xC0, 0x83]
rg = 6.144

#Backpack
backpack_address = 0x70
display_on= 0b10000001
display_off= 0b10000000
system_setup = 0b00100001 

#one letter variable names are bad but we're lazy 
c = Circuit(SMBus(1), adc_address, backpack_address)


#ADC Setup
c.write_block('adc', configr, cb)

#7 Segment Setup
c.write_byte(system_setup) 
c.write_byte(display_on) 
c.update(23)
c.update('clear')
c.write_byte(display_off) 

