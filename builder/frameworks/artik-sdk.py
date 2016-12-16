# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
ARTIK SDK

ARTIK SDK is a C/C++ SDK targeting Samsung ARTIK platforms. It exposes
a set of APIs to ease up development of applications. These APIs cover
hardware buses such as GPIO, SPI, I2C, UART, connectivity links
like Wi-Fi, Bluetooth, Zigbee, and network protocols such as HTTP, Websockets,
MQTT, and others.

http://www.artik.io
"""

from os.path import join, isdir
from os import listdir

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

sdkdir = env.PioPlatform().get_package_dir("framework-artik-sdk")
incdir = join(sdkdir, "include", "artik")
libdir = join(sdkdir, "lib")

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wformat=2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ],

    LIBS=[
        "artik-sdk-base"
    ]
)

env.Append(
    CPPPATH=[
        join(incdir, o) for o in listdir(incdir) if isdir(join(incdir, o))
    ],

    LIBPATH=[
        libdir
    ],

    RPATH=[
        libdir
    ]
)
