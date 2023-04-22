
from machine import I2C,Pin
from time import sleep_ms,sleep_us
import math
# from typing import Tuple


# Gyro = [0, 0, 0]
# Accel = [0, 0, 0]
# Mag = [0, 0, 0]
# MotionVal = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# pitch = 0.0
# roll = 0.0
# yaw = 0.0
# pu8data = [0, 0, 0, 0, 0, 0, 0, 0]
# U8tempX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# U8tempY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# U8tempZ = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# GyroOffset = [0, 0, 0]
# Ki = 1.0
# Kp = 4.50
# q0 = 1.0
# q1 = q2 = q3 = 0.0
# angles = [0.0, 0.0, 0.0]

# true                                 = 0x01
# false                                = 0x00

# define ICM-20948 Device I2C address
I2C_ADR_ICM20948                     = 0x69
I2C_ADR_ICM20948_AK09916             = 0x0C
I2C_ADR_ICM20948_AK09916_READ        = 0x80
I2C_ADR_ICM20948_AK09916_WRITE       = 0x00

# define ICM-20948 Register
# user bank 0 register
REG_ADR_WIA                          = 0x00
REG_VAL_WIA                          = 0xEA
REG_ADR_USER_CTRL                    = 0x03
REG_VAL_BIT_DMP_EN                   = 0x80
REG_VAL_BIT_FIFO_EN                  = 0x40
REG_VAL_BIT_I2C_MST_EN               = 0x20
REG_VAL_BIT_I2C_IF_DIS               = 0x10
REG_VAL_BIT_DMP_RST                  = 0x08
REG_VAL_BIT_DIAMOND_DMP_RST          = 0x04
REG_ADR_LP_CONFIG                    = 0x05
REG_VAL_ALL_RGE_RESET                = 0x80
REG_VAL_RUN_MODE                     = 0x01 # Non low-power mode
REG_ADR_PWR_MGMT_1                   = 0x06
REG_ADR_PWR_MGMT_2                   = 0x07
REG_ADR_INT_ENABLE                   = 0x10
REG_VAL_BIT_DMP_INT1_EN              = 0x02
REG_VAL_BIT_WOM_INT_EN               = 0x08
REG_ADR_INT_STATUS                   = 0x19
REG_ADR_INT_STATUS_1                 = 0x1A
REG_ADR_INT_STATUS_2                 = 0x1B
REG_ADR_INT_STATUS_3                 = 0x1C
REG_ADR_ACCEL_XOUT_H                 = 0x2D
REG_ADR_ACCEL_XOUT_L                 = 0x2E
REG_ADR_ACCEL_YOUT_H                 = 0x2F
REG_ADR_ACCEL_YOUT_L                 = 0x30
REG_ADR_ACCEL_ZOUT_H                 = 0x31
REG_ADR_ACCEL_ZOUT_L                 = 0x32
REG_ADR_GYRO_XOUT_H                  = 0x33
REG_ADR_GYRO_XOUT_L                  = 0x34
REG_ADR_GYRO_YOUT_H                  = 0x35
REG_ADR_GYRO_YOUT_L                  = 0x36
REG_ADR_GYRO_ZOUT_H                  = 0x37
REG_ADR_GYRO_ZOUT_L                  = 0x38
REG_ADR_TEMP_OUT_H                   = 0x39
REG_ADR_TEMP_OUT_L                   = 0x3A
REG_ADR_EXT_SENS_DATA_00             = 0x3B
REG_ADR_REG_BANK_SEL                 = 0x7F
REG_VAL_REG_BANK_0                   = 0x00
REG_VAL_REG_BANK_1                   = 0x10
REG_VAL_REG_BANK_2                   = 0x20
REG_VAL_REG_BANK_3                   = 0x30

# user bank 1 register
# user bank 2 register
REG_ADR_GYRO_SMPLRT_DIV              = 0x00
REG_ADR_GYRO_CONFIG_1                = 0x01
REG_VAL_BIT_GYRO_DLPCFG_2            = 0x10  # bit[5:3]
REG_VAL_BIT_GYRO_DLPCFG_4            = 0x20  # bit[5:3]
REG_VAL_BIT_GYRO_DLPCFG_6            = 0x30  # bit[5:3]
REG_VAL_BIT_GYRO_FS_250DPS           = 0x00  # bit[2:1]
REG_VAL_BIT_GYRO_FS_500DPS           = 0x02  # bit[2:1]
REG_VAL_BIT_GYRO_FS_1000DPS          = 0x04  # bit[2:1]
REG_VAL_BIT_GYRO_FS_2000DPS          = 0x06  # bit[2:1]
REG_VAL_BIT_GYRO_DLPF                = 0x01  # bit[0]
REG_ADR_ACCEL_SMPLRT_DIV_2           = 0x11
REG_ADR_ACCEL_CONFIG                 = 0x14
REG_VAL_BIT_ACCEL_DLPCFG_2           = 0x10  # bit[5:3]
REG_VAL_BIT_ACCEL_DLPCFG_4           = 0x20  # bit[5:3]
REG_VAL_BIT_ACCEL_DLPCFG_6           = 0x30  # bit[5:3]
REG_VAL_BIT_ACCEL_FS_2g              = 0x00  # bit[2:1]
REG_VAL_BIT_ACCEL_FS_4g              = 0x02  # bit[2:1]
REG_VAL_BIT_ACCEL_FS_8g              = 0x04  # bit[2:1]
REG_VAL_BIT_ACCEL_FS_16g             = 0x06  # bit[2:1]
REG_VAL_BIT_ACCEL_DLPF               = 0x01  # bit[0]

# user bank 3 register
REG_ADR_I2C_SLV0_ADDR                = 0x03
REG_ADR_I2C_SLV0_REG                 = 0x04
REG_ADR_I2C_SLV0_CTRL                = 0x05
REG_VAL_BIT_SLV0_EN                  = 0x80
REG_VAL_BIT_MASK_LEN                 = 0x07
REG_ADR_I2C_SLV0_DO                  = 0x06
REG_ADR_I2C_SLV1_ADDR                = 0x07
REG_ADR_I2C_SLV1_REG                 = 0x08
REG_ADR_I2C_SLV1_CTRL                = 0x09
REG_ADR_I2C_SLV1_DO                  = 0x0A

# define ICM-20948 Register  end

# define ICM-20948 MAG Register
REG_ADR_MAG_WIA1                     = 0x00
REG_VAL_MAG_WIA1                     = 0x48
REG_ADR_MAG_WIA2                     = 0x01
REG_VAL_MAG_WIA2                     = 0x09
REG_ADR_MAG_ST2                      = 0x10
REG_ADR_MAG_DATA                     = 0x11
REG_ADR_MAG_CNTL2                    = 0x31
REG_VAL_MAG_MODE_PD                  = 0x00
REG_VAL_MAG_MODE_SM                  = 0x01
REG_VAL_MAG_MODE_10HZ                = 0x02
REG_VAL_MAG_MODE_20HZ                = 0x04
REG_VAL_MAG_MODE_50HZ                = 0x05
REG_VAL_MAG_MODE_100HZ               = 0x08
REG_VAL_MAG_MODE_ST                  = 0x10
# define ICM-20948 MAG Register  end

MAG_DATA_LEN                         = 0x06
EARTH_GRAVITY                        = 9.8065     # Earth's gravity in [m/s^2]
TEMP_SENSITIVITY                     = 333.87


class ICM20948(object):
    def __init__(self, i2c: I2C, i2c_addr = I2C_ADR_ICM20948):
        self._address = i2c_addr
        self._i2c = i2c
        if not self.is_alive():
            print("ICM-20948 not yet alive\n")
            sleep_ms(500)

        # user bank 0 register
        self._write_byte(REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0)
        self._write_byte(REG_ADR_PWR_MGMT_1, REG_VAL_ALL_RGE_RESET)
        sleep_ms(100)
        self._write_byte(REG_ADR_PWR_MGMT_1, REG_VAL_RUN_MODE)
        # user bank 2 register
        self._write_byte(REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_2)
        self._write_byte(REG_ADR_GYRO_SMPLRT_DIV, 0x07)
        self._write_byte(REG_ADR_GYRO_CONFIG_1, REG_VAL_BIT_GYRO_DLPCFG_6 |
                         REG_VAL_BIT_GYRO_FS_1000DPS | REG_VAL_BIT_GYRO_DLPF)
        self._write_byte(REG_ADR_ACCEL_SMPLRT_DIV_2, 0x07)
        self._write_byte(REG_ADR_ACCEL_CONFIG, REG_VAL_BIT_ACCEL_DLPCFG_6 |
                         REG_VAL_BIT_ACCEL_FS_2g | REG_VAL_BIT_ACCEL_DLPF)
        self._accel_norm_factor = math.pow(2,self._read_byte(REG_ADR_ACCEL_CONFIG) >> 1 & 0x03) / (1<<14)
        self._gyro_norm_factor = 250 * (self._read_byte(REG_ADR_GYRO_CONFIG_1) >> 1 & 0x03) / (1<<14)
        # user bank 0 register
        self._write_byte(REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0)
        self._write_byte(REG_ADR_USER_CTRL, REG_VAL_BIT_DMP_EN)
        self._write_byte(REG_ADR_INT_ENABLE, REG_VAL_BIT_DMP_INT1_EN)
        sleep_ms(100)
        self.gyro_offset = (0, 0, 0)
        self.last_raw_accel = (0, 0, 0)
        self.last_raw_gyro = (0, 0, 0)
        self.last_temp = 0
        self.reset_gyro_offset()
        # self.icm20948MagCheck()
        # self.icm20948WriteSecondary(
        #     I2C_ADR_ICM20948_AK09916 | I2C_ADR_ICM20948_AK09916_WRITE, REG_ADR_MAG_CNTL2, REG_VAL_MAG_MODE_20HZ)


    def _read_block(self, register: int, num_bytes: int) -> bytes:
        return self._i2c.readfrom_mem(self._address, register, num_bytes)

    def _read_byte(self, register: int) -> int:
        return self._read_block(register, 1)[0]

    def _read_u16(self, register: int) -> int:
        value = self._read_block(register, 2)
        return self._fix_python_shift_overflow(value[0] << 8 | value[1])


    def _write_byte(self, register: int, value: int) -> None:
        self._i2c.writeto_mem(self._address, register, value.to_bytes(1, 'big'))
        sleep_us(100)


    def is_alive(self):
        return self._read_byte(REG_ADR_WIA) == REG_VAL_WIA


    """Resets the gyroscope offset
    returns the current offset as Tuple[int, int, int]
    """
    def reset_gyro_offset(self):
        self.gyro_offset = (0, 0, 0)
        s32TempGx = 0
        s32TempGy = 0
        s32TempGz = 0
        for i in range(0,32):
            (accel, gyro) = self.read_raw_gyro_accel()
            s32TempGx += gyro[0]
            s32TempGy += gyro[1]
            s32TempGz += gyro[2]
            sleep_ms(10)
        self.gyro_offset = (s32TempGx >> 5, s32TempGy >> 5, s32TempGz >> 5)
        return self.gyro_offset


    """Solve the problem that Python shift will not overflow."""
    def _fix_python_shift_overflow(self, value: int) -> int:
        if value >=32767:
            return value - 65535
        elif value<=-32767:
            return value + 65535
        else:
            return value


    """Read the current raw value for acceleration and gyroscope
    returns Tuple[Tuple[int, int, int], Tuple[int, int, int]]
    """
    def read_raw_gyro_accel(self):
        self._write_byte(REG_ADR_REG_BANK_SEL , REG_VAL_REG_BANK_0)
        data =self._read_block(REG_ADR_ACCEL_XOUT_H, 12)

        accel_x = self._fix_python_shift_overflow((data[0]<<8)|data[1])
        accel_y = self._fix_python_shift_overflow((data[2]<<8)|data[3])
        accel_z = self._fix_python_shift_overflow((data[4]<<8)|data[5])

        gyro_x = self._fix_python_shift_overflow(((data[6]<<8)|data[7]) - self.gyro_offset[0])
        gyro_y = self._fix_python_shift_overflow(((data[8]<<8)|data[9]) - self.gyro_offset[1])
        gyro_z = self._fix_python_shift_overflow(((data[10]<<8)|data[11]) - self.gyro_offset[2])

        self.last_raw_accel = (accel_x, accel_y, accel_z)
        self.last_raw_gyro = (gyro_x, gyro_y, gyro_z)
        return (self.last_raw_accel, self.last_raw_gyro)

    def read_norm_accel(self, do_update = False):
        if do_update:
            self.read_raw_gyro_accel()
        return tuple(self._accel_norm_factor * val for val in self.last_raw_accel)

    def read_norm_gyro(self, do_update = False):
        if do_update:
            self.read_raw_gyro_accel()
        return tuple(self._gyro_norm_factor * val for val in self.last_raw_gyro)

    def read_norm_gyro_accel(self, do_update = True):
        return (self.read_norm_accel(do_update), self.read_norm_gyro())


    def read_raw_temp(self) -> int:
        self._write_byte(REG_ADR_REG_BANK_SEL , REG_VAL_REG_BANK_0)
        self.last_temp = self._read_u16(REG_ADR_TEMP_OUT_H)
        return self.last_temp

    def read_norm_temp(self, do_update = True) -> float:
        if do_update:
            self.read_raw_temp()
        return self.last_temp / TEMP_SENSITIVITY + 21


#   def icm20948MagRead(self):
#     counter=20
#     while(counter>0):
#       time.sleep(0.01)
#       self.icm20948ReadSecondary( I2C_ADR_ICM20948_AK09916|I2C_ADR_ICM20948_AK09916_READ , REG_ADR_MAG_ST2, 1)
#       if ((pu8data[0] & 0x01)!= 0):
#         break
#       counter-=1
#     if counter!=0:
#       for i in range(0,8):
#         self.icm20948ReadSecondary( I2C_ADR_ICM20948_AK09916|I2C_ADR_ICM20948_AK09916_READ , REG_ADR_MAG_DATA , MAG_DATA_LEN)
#         U8tempX[i] = (pu8data[1]<<8)|pu8data[0]
#         U8tempY[i] = (pu8data[3]<<8)|pu8data[2]
#         U8tempZ[i] = (pu8data[5]<<8)|pu8data[4]
#       Mag[0]=(U8tempX[0]+U8tempX[1]+U8tempX[2]+U8tempX[3]+U8tempX[4]+U8tempX[5]+U8tempX[6]+U8tempX[7])/8
#       Mag[1]=-(U8tempY[0]+U8tempY[1]+U8tempY[2]+U8tempY[3]+U8tempY[4]+U8tempY[5]+U8tempY[6]+U8tempY[7])/8
#       Mag[2]=-(U8tempZ[0]+U8tempZ[1]+U8tempZ[2]+U8tempZ[3]+U8tempZ[4]+U8tempZ[5]+U8tempZ[6]+U8tempZ[7])/8
#     if Mag[0]>=32767:            #Solve the problem that Python shift will not overflow
#       Mag[0]=Mag[0]-65535
#     elif Mag[0]<=-32767:
#       Mag[0]=Mag[0]+65535
#     if Mag[1]>=32767:
#       Mag[1]=Mag[1]-65535
#     elif Mag[1]<=-32767:
#       Mag[1]=Mag[1]+65535
#     if Mag[2]>=32767:
#       Mag[2]=Mag[2]-65535
#     elif Mag[2]<=-32767:
#       Mag[2]=Mag[2]+65535
#   def icm20948ReadSecondary(self,u8I2CAddr,u8RegAddr,u8Len):
#     u8Temp=0
#     self._write_byte( REG_ADR_REG_BANK_SEL,  REG_VAL_REG_BANK_3) #swtich bank3
#     self._write_byte( REG_ADR_I2C_SLV0_ADDR, u8I2CAddr)
#     self._write_byte( REG_ADR_I2C_SLV0_REG,  u8RegAddr)
#     self._write_byte( REG_ADR_I2C_SLV0_CTRL, REG_VAL_BIT_SLV0_EN|u8Len)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0) #swtich bank0

#     u8Temp = self._read_byte(REG_ADR_USER_CTRL)
#     u8Temp |= REG_VAL_BIT_I2C_MST_EN
#     self._write_byte( REG_ADR_USER_CTRL, u8Temp)
#     time.sleep(0.01)
#     u8Temp &= ~REG_VAL_BIT_I2C_MST_EN
#     self._write_byte( REG_ADR_USER_CTRL, u8Temp)

#     for i in range(0,u8Len):
#       pu8data[i]= self._read_byte( REG_ADR_EXT_SENS_DATA_00+i)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_3) #swtich bank3

#     u8Temp = self._read_byte(REG_ADR_I2C_SLV0_CTRL)
#     u8Temp &= ~((REG_VAL_BIT_I2C_MST_EN)&(REG_VAL_BIT_MASK_LEN))
#     self._write_byte( REG_ADR_I2C_SLV0_CTRL,  u8Temp)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0) #swtich bank0
#   def icm20948WriteSecondary(self,u8I2CAddr,u8RegAddr,u8data):
#     u8Temp=0
#     self._write_byte( REG_ADR_REG_BANK_SEL,  REG_VAL_REG_BANK_3) #swtich bank3
#     self._write_byte( REG_ADR_I2C_SLV1_ADDR, u8I2CAddr)
#     self._write_byte( REG_ADR_I2C_SLV1_REG,  u8RegAddr)
#     self._write_byte( REG_ADR_I2C_SLV1_DO,   u8data)
#     self._write_byte( REG_ADR_I2C_SLV1_CTRL, REG_VAL_BIT_SLV0_EN|1)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0) #swtich bank0

#     u8Temp = self._read_byte(REG_ADR_USER_CTRL)
#     u8Temp |= REG_VAL_BIT_I2C_MST_EN
#     self._write_byte( REG_ADR_USER_CTRL, u8Temp)
#     time.sleep(0.01)
#     u8Temp &= ~REG_VAL_BIT_I2C_MST_EN
#     self._write_byte( REG_ADR_USER_CTRL, u8Temp)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_3) #swtich bank3

#     u8Temp = self._read_byte(REG_ADR_I2C_SLV0_CTRL)
#     u8Temp &= ~((REG_VAL_BIT_I2C_MST_EN)&(REG_VAL_BIT_MASK_LEN))
#     self._write_byte( REG_ADR_I2C_SLV0_CTRL,  u8Temp)

#     self._write_byte( REG_ADR_REG_BANK_SEL, REG_VAL_REG_BANK_0) #swtich bank0
#   def icm20948GyroOffset(self):
#     s32TempGx = 0
#     s32TempGy = 0
#     s32TempGz = 0
#     for i in range(0,32):
#       self.icm20948_Gyro_Accel_Read()
#       s32TempGx += Gyro[0]
#       s32TempGy += Gyro[1]
#       s32TempGz += Gyro[2]
#       time.sleep(0.01)
#     GyroOffset[0] = s32TempGx >> 5
#     GyroOffset[1] = s32TempGy >> 5
#     GyroOffset[2] = s32TempGz >> 5
#   def _read_byte(self,cmd):
#     rec=self._bus.readfrom_mem(int(self._address),int(cmd),1)
#     return rec[0]
#   def _read_block(self, reg, length=1):
#     rec=self._bus.readfrom_mem(int(self._address),int(reg),length)
#     return rec
#   def _read_u16(self,cmd):
#     LSB = self._bus.readfrom_mem(int(self._address),int(cmd),1)
#     MSB = self._bus.readfrom_mem(int(self._address),int(cmd)+1,1)
#     return (MSB[0] << 8) + LSB[0]

#   def _write_byte(self,cmd,val):
#     self._bus.writeto_mem(int(self._address),int(cmd),bytes([int(val)]))
#     time.sleep(0.0001)
#   def imuAHRSupdate(self,gx, gy,gz,ax,ay,az,mx,my,mz):
#     norm=0.0
#     hx = hy = hz = bx = bz = 0.0
#     vx = vy = vz = wx = wy = wz = 0.0
#     exInt = eyInt = ezInt = 0.0
#     ex=ey=ez=0.0
#     halfT = 0.024
#     global q0
#     global q1
#     global q2
#     global q3
#     q0q0 = q0 * q0
#     q0q1 = q0 * q1
#     q0q2 = q0 * q2
#     q0q3 = q0 * q3
#     q1q1 = q1 * q1
#     q1q2 = q1 * q2
#     q1q3 = q1 * q3
#     q2q2 = q2 * q2
#     q2q3 = q2 * q3
#     q3q3 = q3 * q3

#     norm = float(1/math.sqrt(ax * ax + ay * ay + az * az))
#     ax = ax * norm
#     ay = ay * norm
#     az = az * norm

#     norm = float(1/math.sqrt(mx * mx + my * my + mz * mz))
#     mx = mx * norm
#     my = my * norm
#     mz = mz * norm

#     # compute reference direction of flux
#     hx = 2 * mx * (0.5 - q2q2 - q3q3) + 2 * my * (q1q2 - q0q3) + 2 * mz * (q1q3 + q0q2)
#     hy = 2 * mx * (q1q2 + q0q3) + 2 * my * (0.5 - q1q1 - q3q3) + 2 * mz * (q2q3 - q0q1)
#     hz = 2 * mx * (q1q3 - q0q2) + 2 * my * (q2q3 + q0q1) + 2 * mz * (0.5 - q1q1 - q2q2)
#     bx = math.sqrt((hx * hx) + (hy * hy))
#     bz = hz

#     # estimated direction of gravity and flux (v and w)
#     vx = 2 * (q1q3 - q0q2)
#     vy = 2 * (q0q1 + q2q3)
#     vz = q0q0 - q1q1 - q2q2 + q3q3
#     wx = 2 * bx * (0.5 - q2q2 - q3q3) + 2 * bz * (q1q3 - q0q2)
#     wy = 2 * bx * (q1q2 - q0q3) + 2 * bz * (q0q1 + q2q3)
#     wz = 2 * bx * (q0q2 + q1q3) + 2 * bz * (0.5 - q1q1 - q2q2)

#     # error is sum of cross product between reference direction of fields and direction measured by sensors
#     ex = (ay * vz - az * vy) + (my * wz - mz * wy)
#     ey = (az * vx - ax * vz) + (mz * wx - mx * wz)
#     ez = (ax * vy - ay * vx) + (mx * wy - my * wx)

#     if (ex != 0.0 and ey != 0.0 and ez != 0.0):
#       exInt = exInt + ex * Ki * halfT
#       eyInt = eyInt + ey * Ki * halfT
#       ezInt = ezInt + ez * Ki * halfT

#       gx = gx + Kp * ex + exInt
#       gy = gy + Kp * ey + eyInt
#       gz = gz + Kp * ez + ezInt

#     q0 = q0 + (-q1 * gx - q2 * gy - q3 * gz) * halfT
#     q1 = q1 + (q0 * gx + q2 * gz - q3 * gy) * halfT
#     q2 = q2 + (q0 * gy - q1 * gz + q3 * gx) * halfT
#     q3 = q3 + (q0 * gz + q1 * gy - q2 * gx) * halfT

#     norm = float(1/math.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3))
#     q0 = q0 * norm
#     q1 = q1 * norm
#     q2 = q2 * norm
#     q3 = q3 * norm
#   def icm20948Check(self):
#     bRet=false
#     if REG_VAL_WIA == self._read_byte(REG_ADR_WIA):
#       bRet = true
#     return bRet
#   def icm20948MagCheck(self):
#     self.icm20948ReadSecondary( I2C_ADR_ICM20948_AK09916|I2C_ADR_ICM20948_AK09916_READ,REG_ADR_MAG_WIA1, 2)
#     if (pu8data[0] == REG_VAL_MAG_WIA1) and ( pu8data[1] == REG_VAL_MAG_WIA2) :
#         bRet = true
#         return bRet
#   def icm20948CalAvgValue(self):
#     MotionVal[0]=Gyro[0]/32.8
#     MotionVal[1]=Gyro[1]/32.8
#     MotionVal[2]=Gyro[2]/32.8
#     MotionVal[3]=Accel[0]
#     MotionVal[4]=Accel[1]
#     MotionVal[5]=Accel[2]
#     MotionVal[6]=Mag[0]
#     MotionVal[7]=Mag[1]
#     MotionVal[8]=Mag[2]
#   def update(self):
#     self.icm20948_Gyro_Accel_Read()
#     self.icm20948MagRead()
#     self.icm20948CalAvgValue()
#     self.imuAHRSupdate(MotionVal[0] * 0.0175, MotionVal[1] * 0.0175,MotionVal[2] * 0.0175, MotionVal[3],MotionVal[4],MotionVal[5], MotionVal[6], MotionVal[7], MotionVal[8])
#     pitch = math.asin(-2 * q1 * q3 + 2 * q0* q2)* 57.3
#     roll  = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)* 57.3
#     yaw   = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3
#     return (yaw, roll, pitch, Accel, Gyro, Mag)

# if __name__ == '__main__':
#   import time
#   print("\nSense HAT Test Program ...\n")
#   MotionVal=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#   icm20948=ICM20948()
#   while True:
#     icm20948.icm20948_Gyro_Accel_Read()
#     icm20948.icm20948MagRead()
#     icm20948.icm20948CalAvgValue()
#     time.sleep(0.1)
#     icm20948.imuAHRSupdate(MotionVal[0] * 0.0175, MotionVal[1] * 0.0175,MotionVal[2] * 0.0175, MotionVal[3],MotionVal[4],MotionVal[5], MotionVal[6], MotionVal[7], MotionVal[8])
#     pitch = math.asin(-2 * q1 * q3 + 2 * q0* q2)* 57.3
#     roll  = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)* 57.3
#     yaw   = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3
#     print("\r\n /-------------------------------------------------------------/ \r\n")
#     print('\r\n Roll = %.2f , Pitch = %.2f , Yaw = %.2f\r\n'%(roll,pitch,yaw))
#     print('\r\nAcceleration:  X = %d , Y = %d , Z = %d\r\n'%(Accel[0],Accel[1],Accel[2]))
#     print('\r\nGyroscope:     X = %d , Y = %d , Z = %d\r\n'%(Gyro[0],Gyro[1],Gyro[2]))
#     print('\r\nMagnetic:      X = %d , Y = %d , Z = %d'%((Mag[0]),Mag[1],Mag[2]))
