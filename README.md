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
	$ python lifx.py <device MAC address> <device IP address> <command>
	```

	Where:

	* ``<device MAC address>`` - MAC address of the device to command, e.g. 01:23:45:67:89:0a
	* ``<device IP address>`` - IP address of the device to command, e.g. 192.123.45.67
	* ``<command>`` - The command to perform

	Where ``<command>`` is one of:

	* ``power_off`` - turn off the device
	* ``power_on`` - turn on the device

## Compiling to Windows executable

Compile using:

```
$ pyinstaller --onefile lifx.py
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
