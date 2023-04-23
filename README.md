# Projekt G-G-Meter

Ziel des Projekts ist ein G-G-Meter zum Motorrad zu entwickeln.
Ein G-G-Meter zeichnet die Beschleunigung des Motorades in Fahrtrichtung und
Quer dazu auf, jeweils normal zur Erdbeschleunigung.

## Hardware

Die Hardware besteht aus:
* [Pimoroni Tiny 2040](https://shop.pimoroni.com/products/tiny-2040)
* [Waveshare 1.54" ePaper](https://www.waveshare.com/wiki/1.54inch_e-Paper_Module_Manual)
  * [Datenblatt](https://www.waveshare.com/w/upload/e/e5/1.54inch_e-paper_V2_Datasheet.pdf)
* [Adafruit TDK InvenSense ICM-20948 9-DoF IMU](https://learn.adafruit.com/adafruit-tdk-invensense-icm-20948-9-dof-imu/pinouts)
  * [Adafruit Datasheet](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-tdk-invensense-icm-20948-9-dof-imu.pdf)
  * [TDK Datenblatt](https://invensense.tdk.com/wp-content/uploads/2021/10/DS-000189-ICM-20948-v1.5.pdf)




## Ressourcen
* [Raspberry Pi Pico (RP2040) I2C Example with MicroPython and C/C++](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-i2c-example-with-micropython-and-cc/47d0c922b79342779cdbd4b37b7eb7e2)
* [How to Fuse Motion Sensor Data into AHRS Orientation (Euler/Quaternions)](https://learn.adafruit.com/how-to-fuse-motion-sensor-data-into-ahrs-orientation-euler-quaternions/lets-fuse)
* GitHub
  * [laughingrice/ICM20948](https://github.com/laughingrice/ICM20948)
  * [SparkFun_ICM-20948_ArduinoLibrary](https://github.com/sparkfun/SparkFun_ICM-20948_ArduinoLibrary)
  * [Arduino_ICM20948_DMP_Full](https://github.com/isouriadakis/Arduino_ICM20948_DMP_Full-Function)
  * [morgil/madgwick_py](https://github.com/morgil/madgwick_py/blob/master/madgwickahrs.py)
