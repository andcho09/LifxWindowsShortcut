"""
Controls Lifx devices via LAN API
"""

import argparse
from os import name
import lifxlan
import sys

def main():
	parser = argparse.ArgumentParser(description='Control Lifx Device via LAN')
	parser.add_argument('mac', help='Lifx device MAC address, e.g. 01:23:45:67:89:0a')
	parser.add_argument('ip', help='Lifx device IP address, e.g. 192.123.45.67')
	subparsers = parser.add_subparsers(dest='subcommand', required=True)

	parser_power = subparsers.add_parser('power', help='Powers on/off the device')
	parser_power.set_defaults(func=_power_command)
	parser_power.add_argument('on/off', choices=['on', 'off'])

	parser_get_power = subparsers.add_parser('get_power', help='Retrieves device power level')
	parser_get_power.set_defaults(func=_get_power_command)

	parser_colour = subparsers.add_parser('colour', help='Changes device colour. See https://lan.developer.lifx.com/docs/representing-color-with-hsbk for values.')
	parser_colour.set_defaults(func=_colour_command)
	parser_colour.add_argument('hue', type=ClampedFloat(0, 360), help="Hue from 0 to 360")
	parser_colour.add_argument('saturation', type=ClampedFloat(0, 1), help="Saturation from 0 (white) to 1 (full colour)")
	parser_colour.add_argument('brightness', type=ClampedFloat(0, 1), help="Brightness from 0 (off) to 1 (full power)")
	parser_colour.add_argument('kelvin', type=ClampedFloat(1500, 9000), help="Kelvin from 2500 to 9000")

	parser_get_colour = subparsers.add_parser('get_colour', help='Retrieves device colour in HSBK list format')
	parser_get_colour.set_defaults(func=_get_colour_command)

	args = parser.parse_args()
	args.func(vars(args))

def _power_command(args_dict):
	light = lifxlan.Light(args_dict['mac'], args_dict['ip'])
	light.set_power(args_dict['on/off'])

def _get_power_command(args_dict):
	light = lifxlan.Light(args_dict['mac'], args_dict['ip'])
	print('off' if light.get_power() == 0 else 'on')

def _colour_command(args_dict):
	light = lifxlan.Light(args_dict['mac'], args_dict['ip'])
	hue = int(round(0x10000 * args_dict['hue']) / 360) % 0x10000
	saturation = int(round(0xFFFF * args_dict['saturation']))
	brightness = int(round(0xFFFF * args_dict['brightness']))
	light.set_color([hue, saturation, brightness, args_dict['kelvin']])

def _get_colour_command(args_dict):
	light = lifxlan.Light(args_dict['mac'], args_dict['ip'])
	hsbk = light.get_color()
	print(hsbk)
	print(f"{round(float(hsbk[0]) * 360 / 0x10000, 2)}, {round(float(hsbk[1]) / 0xFFFF, 4)}, {round(float(hsbk[2]) / 0xFFFF, 4)}, {hsbk[3]}")

"""
Returns an float representation of the value, or an error if it is not in the valid range
"""
class ClampedFloat(object):

	def __init__(self, min, max):
		self.min = min
		self.max = max

	def __call__(self, value):
		return_value = float(value)
		if return_value < self.min or return_value > self.max:
			message = f"'{value}' is not a float between {self.min} and {self.max}"
			print(f"ERROR: {message}")
			raise argparse.ArgumentError(message)
		return return_value

if __name__=="__main__":
	main()