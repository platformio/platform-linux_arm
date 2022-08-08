How to build PlatformIO based project
=====================================

1. [Install PlatformIO Core](https://docs.platformio.org/page/core.html)
2. Download [development platform with examples](https://github.com/platformio/platform-linux_arm/archive/develop.zip)
3. Extract ZIP archive
4. Run these commands:

```shell
# Change directory to example
$ cd platform-linux_arm/examples/wiringpi-serial

# Build project
$ pio run

# Run program
> .pio/raspberrypi_2b/program

# Clean build files
$ pio run --target clean
```
