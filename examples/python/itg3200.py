# Author: Sarah Knepper <sarah.knepper@intel.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
import pyupm_itg3200 as itg3200

# load this on i2c
gyro = itg3200.Itg3200(0)

# Note: Sensor not supported on Intel Edison with Arduino breakout
while 1:
    gyro.update(); # Update the data
    rot = gyro.getRawValues(); # Read raw sensor data
    ang = gyro.getRotation(); # Read rotational speed (deg/sec)
    temp = gyro.getTemperature();
    raw = gyro.getRawTemp();
    print "Raw: %6d %6d %6d" % (rot[0], rot[1], rot[2]);
    print "AngX: %5.2f" % (ang[0]);
    print "AngY: %5.2f" % (ang[1]);
    print "AngZ: %5.2f" % (ang[2]);
    print "Temp: %5.2f Raw: %6d" % (temp, raw);
    time.sleep(1)

# Delete the gyro object
del gyro
