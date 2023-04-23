# hw_setup.py Customise for your hardware config

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2020 Peter Hinch

# As written, supports:
# Adafruit 1.5" 128*128 OLED display: https://www.adafruit.com/product/1431
# Adafruit 1.27" 128*96 display https://www.adafruit.com/product/1673
# Edit the driver import for other displays.

# Demo of initialisation procedure designed to minimise risk of memory fail
# when instantiating the frame buffer. The aim is to do this as early as
# possible before importing other modules.

# WIRING (Adafruit pin nos and names).
# Pyb   SSD
# 3v3   Vin (10)
# Gnd   Gnd (11)
# Y1    DC (3 DC)
# Y2    CS (5 OC OLEDCS)
# Y3    Rst (4 R RESET)
# Y6    CLK (2 CL SCK)
# Y8    DATA (1 SI MOSI)

from machine import Pin,SPI,I2C
import gc
# from icm20948_i2c import ICM20948


# *** Choose your color display driver here ***
# Driver supporting non-STM platforms
# from drivers.ssd1351.ssd1351_generic import SSD1351 as SSD

# STM specific driver
from drivers.epaper.epd1in54_V2_fb import EPD as SSD

#height = 96  # 1.27 inch 96*128 (rows*cols) display
#height = 128 # 1.5 inch 128*128 display
height = 200

### Raspberry Pi PICO
# ssd_spi = SPI(0, baudrate=16000_000, sck=Pin(18), mosi=Pin(19))
# ssd_cs = Pin(17)
# ssd_dc = Pin(16)
# ssd_rst = Pin(20)
# ssd_busy = Pin(21)

### Pimoroni Tiny 2040
# ssd_spi = SPI(0, baudrate=16000_000, sck=Pin(2), mosi=Pin(3), miso=Pin(0))
# ssd_cs = Pin(1)
# ssd_dc = Pin(4)
# ssd_rst = Pin(5)
# ssd_busy = Pin(6)
# imu_i2c = I2C(1, scl=Pin(27), sda=Pin(26))
# imu_int = Pin(7)
led_b=Pin(20, Pin.OUT)
led_r=Pin(18, Pin.OUT)
led_g=Pin(19, Pin.OUT)

led_r.on()
led_g.on()
led_b.on()

# gc.collect()  # Precaution before instantiating framebuf
# ssd = SSD(ssd_spi, ssd_cs, ssd_dc, ssd_rst, ssd_busy)  # Create a display instance


def imu_int_irq(pin):
    global led_r
    led_r.toggle()

imu_i2c = I2C(1, scl=Pin(27), sda=Pin(26))
imu_int = Pin(7)
imu_int.irq(trigger=Pin.IRQ_RISING, handler=imu_int_irq)


# imu = ICM20948(imu_i2c)
from lib.drivers.ICM20948.ICM20948 import ICM20948
from lib.drivers.ICM20948.bus import I2C_Bus
imu = ICM20948()
for i in range(10):
    try:
        imu._setup(I2C_Bus(imu_i2c))
    except Exception as e:
        print('got exception: {} - trying again'.format(e))

    if imu.AK09916_initialized:
        break
