# Lifx Windows Shortcut

Builds Windows executable to quick access Lifx Bulb functions.


## Usage

Note this is a Windows project as executables can only be created on the same platform.

### First-time setup

1. Create virtualenv

	```
	$ python -m venv .venv
	$ .venv\Scripts\activate.bat
	```

1. Install dependencies

	```
	$ pip install -r requirements.txt
	```

### Python script usage

1. Switch to virtualenv

	```
	$ .venv\Scripts\activate.bat
	```

1. Run python script

	```
	$ python lifx.py <device MAC address> <device IP address> <subcommand>
	```

	Where:

	* ``<device MAC address>`` - MAC address of the device to command, e.g. 01:23:45:67:89:0a
	* ``<device IP address>`` - IP address of the device to command, e.g. 192.123.45.67
	* ``<command>`` - One of the following subcommands:
		* ``power`` - Controls the device power state
			* ``on/off`` - Use ``on`` or ``off`` to power on and off the device
		* ``colour`` - Controls the device colour. See [Representing Color with HSBK](https://lan.developer.lifx.com/docs/representing-color-with-hsbk) for details
			* ``hue`` - Hue from 0 to 360. Red = 0, green = 120
			* ``saturation`` - Saturation from 0 (white) to 1 (full colour)
			* ``brightness`` - Brightness from 0 (off) to 1 (full power)
			* ``kelvin`` - Kelvin from 1500 to 9000
		* ``get_colour`` - Retrieves the device's colour as a list of [hue, saturation, brightness, kelvin]

	Examples:

	* Power on the device

		```
		$ python lifx.py 01:23:45:67:89:0a 192.123.45.67 power on
		```

	* Set the colour of the device to a very warm midnight level

		```
		$ python lifx.py 01:23:45:67:89:0a 192.123.45.67 colour 15 0 0.25 1500
		```

	* Set the colour of the device to a warm evening level

		```
		$ python lifx.py 01:23:45:67:89:0a 192.123.45.67 colour 15 0 0.7 2000
		```


## Compiling to Windows executable

Compile using:

```
$ pyinstaller --onefile --icon lifx.ico lifx.py
```

Executable will be in ``dist``

## Troubleshooting

### Error loading Python DLL message  when running .exe

**Looks like:** An error message similar to:

> Error loading Python DLL 'D:\Users\Andrew\Downloads\python38.dll'.

**Caused by:** ``python<version>.dll`` must be in the same directory as the .exe or on the PATH

**Resolve by:** Add Python 3 directory to path

### How do you find the Lifx device's MAC address and IP address?

**Resolve by:** In router DHCP configuration, look for a ``LIFX...`` device

### Can't pin shortcuts to Windows Start menu multiple times

**Looks like:** Pinning a shortcut to the start menu doesn't work or creates a blank broken tile

**Resolve by:** Don't copy-paste shortcuts. Create new ones each time you pin a shortcut