#/usr/bin/python3
from i2c_writer import *
import lights, sys, time

#ADC
adc_address = 0x48
configr= 0x01
conversionr= 0x00
cb = [0xC0, 0x83]
rg = 6.144

#Backpack
backpack_address = 0x70
blink_setup = 1000001
system_setup = 100001 #00100001

bus = SMBus(1)
write_register(bus, adc_address, configr, conversionr, cb)

write_byte(bus, backpack_address, system_setup) 
write_byte(bus, backpack_address, blink_setup) 


