#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0 , 255)
indigo = (0, 255, 255)
white = (255, 255 ,255)
brown = (139, 69, 19)
p_text = raw_input("What message would you like? ")
p_color = input("What color would you like your text? ")
p_speed = input("What speed would you like? ( >1 = fast, <1 = slow) ")
sense.show_message(p_text, text_colour = p_color, scroll_speed = p_speed)
