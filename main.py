import lib.gui.core.nanogui as NG
from lib.hw_setup import ssd,imu
import time

NG.circle(ssd, 80, 80, 75, 1)
ssd.show()

# while True:
#     print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (imu.acceleration))
#     print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (imu.gyro))
#     print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (imu.magnetic))
#     print("")
#     time.sleep(0.5)


