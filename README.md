# Linux ARM: development platform for [PlatformIO](http://platformio.org)

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X, Linux ARM) you can build native application for Linux ARM platform.

* [Home](http://platformio.org/platforms/linux_arm) (home page in PlatformIO Platform Registry)
* [Documentation](http://docs.platformio.org/page/platforms/linux_arm.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = linux_arm
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-linux_arm.git
board = ...
...
```

# Configuration

Please navigate to [documentation](http://docs.platformio.org/page/platforms/linux_arm.html).
