# Python LWRF

Control Lightwave RF Devices using Python

## Versions of LWRF Kit

This libary currently only supports Version 1 Lightwave Devices,
and therefore will only return whether it has been able to send the packet to
the network, not whether the device reacted or not.

The shortcoming of 2-way communication has been resolved by LightwaveRF in
Version 2 of their hardware, however I do not currently have the ability to
test this as I do not have access to the hardware.

## Installation

As with most python libraries, we recommend that you work in a virtual
environment when using this library.

Either clone this repository and run `python setup.py install`, or install from
pip using `pip install python-lwrf`.

## Usage

A sample script to pair with your LWRF WiFi Hub, turn on the first light in the first room of your house,
set the brightness to 100%, dim the light to 50%, increase it to 100% again,
and then turn the light off could look as follows:

```python
#!/usr/bin/env python3

import time
from lwrf.v1.hub import Hub
from lwrf.v1.light import Light

hub_ip_address = 10.10.10.10.1
hub_port = 9670

my_hub = Hub(hub_ip_address, hub_port)
my_hub.link_hub() # The hub should enter "link" mode, see the manual for your
                  # hub for specific instructions on how to link your devices
lamp = Light(my_hub, room_id=1, device_id=1)

lamp.change_state('ON')
time.sleep(1)
lamp.change_state('OFF')
time.sleep(1)
print(lamp.change_state('DIM', 32))
time.sleep(1)
print(lamp.change_state('DIM', 16))
time.sleep(1)
print(lamp.change_state('DIM', 32))
time.sleep(1)
lamp.change_state('OFF')
```
