#!/usr/bin/python3
from configure import *
from backpack import *
import lights, sys, time

da = 0x48
configr= 0x01
conversionr= 0x00
cb = [0xC0, 0x83]
rg = 6.144

blink_setup = 1000000
system_setup = 100001 #00100001

bus = SMBus(1)
configure_adc(bus, da, configr, conversionr, cb)

shove_backpack(bus, blink_setup) 
shove_backpack(bus, system_setup) 
q = get_raw_adc_reading(bus)


