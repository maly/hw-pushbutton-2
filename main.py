from microbit import *

# nastavení pinů

while True:
    if pins.digital_read_pin(DigitalPin.P2) == 1:  # pokud je tlačítko stisknuto
        if pins.digital_read_pin(DigitalPin.P2) == 1 and pins.analog_read_pin(AnalogPin.P0) == 0:  # pokud je tlačítko stisknuto a LED vypnuta
            pins.analog_write_pin(AnalogPin.P1,pins.analog_read_pin(AnalogPin.P0))  # zapne LED s jasem nastaveným potenciometrem
        else:
            pins.analog_write_pin(AnalogPin.P1,0)  # vypne LED
    else:
        pins.analog_write_pin(AnalogPin.P1,pins.analog_read_pin(AnalogPin.P0))  # regulace jasu LED pomocí potenciometru
    