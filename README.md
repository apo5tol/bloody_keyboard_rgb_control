# RGB control for A4Tech Bloody keyboard for Linux

[![PyPI version](https://badge.fury.io/py/rgb-control.svg)](https://badge.fury.io/py/rgb-control)

> This script allows you to set the RGB backlight color on A4Tech Bloody keyboards.

### How to use:

- On the keyboard press `Fn` + `1`.
- Make sure you are a sudo user.
- Run the script:
```console
$ rgb-control -c ff0000
```

### Installing
```console
$ python -m pip install rgb-control
```

### Optional arguments:
``` console
-c    - color in hex format. Example: 00ff00 #green
-id_v - vendor id in hex format, default: 0x09DA  
-id_p - product id in hex format, default: 0xFA10  
```

