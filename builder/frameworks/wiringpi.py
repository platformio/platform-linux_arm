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
WiringPi

WiringPi is a GPIO access library written in C for the BCM2835 used in the
Raspberry Pi. It's designed to be familiar to people who have used the Arduino
"wiring" system.

http://wiringpi.com
"""

from os.path import join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wformat=2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ],

    LIBS=["pthread"]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    CPPPATH=[
        join(env.PioPlatform().get_package_dir(
             "framework-wiringpi"), "wiringPi")
    ]
)


#
# Target: Build Core Library
#

libs = []
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkWiringPi"),
    join(env.PioPlatform().get_package_dir("framework-wiringpi"), "wiringPi")
))

env.Append(LIBS=libs)
