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
#rowint will be added to our segment selection each time
rowint_base = 0b10100000 
display_on= 0b10000001
display_off= 0b10000000
system_setup = 0b00100001 

#one letter variable names are bad but the code is
#so short it doesn't really matter
c = Circuit(SMBus(1), adc_address, backpack_address, rowint_base)


#ADC Setup
c.write_block('adc', configr, cb)

#7 Segment Setup
c.write_byte('backpack', system_setup) 
c.write_byte('backpack', display_on) 
time.sleep(2)
c.write_byte('backpack', display_off) 




