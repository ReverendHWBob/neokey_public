# This example is for the NeoKey,
# Limited storage.


import board
import storage, time
import neopixel
from digitalio import DigitalInOut, Pull

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
pixel.fill(0x0)

print("NeoKey boot fooling")
print("Hold the key down to enable storage")
time.sleep(1.4)


# on the NeoKey we use a PULL down)


button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)


if not button .value:
   pixel .fill(0x0000FF) # Blue
   print("Button Pressed, disable storage")
   storage.disable_usb_drive()




