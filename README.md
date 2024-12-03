## Neokey

![Adafruit Trinkey product/5020](https://cdn-learn.adafruit.com/assets/assets/000/102/137/small360/adafruit_products_NeoKey_top_angle_key.jpg?1620935658)

## A functional macropad with the Adafruit Neokey Trinkey
<a href="https://www.adafruit.com/product/5020">Adafruit Neokey Trinket</a>

The Adafruit Neokey Trinkey is a small usb trinket with a ATSAMD21E18 32-bit microcontroller, a neo-pixle, space for a MX compatable key switch, and a small copper pad used for capacitive touch sensing.

### SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries

I don't own this code, I borrowed most of it from the creators of the adafruit Neokey, the rest is regular, delibertly simple python, follwing the KISS principal.
I did create a seperate maco "class" to hold data, which looks a whole lot like the Adafruit Macropad data (why recreate the wheel).

Microcontrollers (especially the neokey's mc) do not have much memory. there is 47KB (kilobytes) of beastly code memory on a blank neokey. Keep your code as short as possible and remember comments take up memory...

Features.
1. macro.py: Python class holding 2 macros, one for the Key switch, one for the Touch switch.
2. boot.py: Turns off the usb-storage drive. Prevent virus tools from looking and bitlocker or other encryptors prompting to encrpyt the drive on ever powerup. (bypass usb disable by pressing and holding the key at powerup. 
3. Code additions to support macro autotype and manage race conditions around the press and release of keys.
