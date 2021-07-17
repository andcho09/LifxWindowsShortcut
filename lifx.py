"""
Controls Lifx devices.
"""

import lifxlan
import sys

def main():
	if len(sys.argv) < 4: # First argument is script name
		print(f'ERROR: Expect at least 3 arguments (<device MAC address> <device IP address> <command>) but only received {len(sys.argv)} arguments')
	light = lifxlan.Light(sys.argv[1], sys.argv[2])
	command = str(sys.argv[3]).lower()
	if command == 'power_on':
		light.set_power('on')
	elif command == 'power_off':
		light.set_power('off')
	else:
		print(f"ERROR: Unknown command '{command}'")

if __name__=="__main__":
	main()