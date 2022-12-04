import time
import time
import board
import pwmio
from adafruit_motor import servo
import adafruit_mpu6050
import math

# create a PWMOut object on Pins
pwm0 = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo0 = servo.Servo(pwm0)
my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)


i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mpu = adafruit_mpu6050.MPU6050(i2c)

gyroAngleX = 90
gyroAngleY = 90
gyroAngleZ = 90
now = time.monotonic()
yaw = 0
pitch = 0
roll = 0

errorX = 0.5
errorY = 0.5
errorZ = 0.5

while True:
    prevtime = now
    now = time.monotonic()
    elapsedTime = now - prevtime

    gyroAngleX = gyroAngleX + math.ceil(math.degrees((mpu.gyro[0]) * elapsedTime) - errorX)
    gyroAngleY = gyroAngleY + math.ceil(math.degrees((mpu.gyro[1]) * elapsedTime) - errorY)
    gyroAngleZ = gyroAngleZ + math.ceil(math.degrees((mpu.gyro[2]) * elapsedTime) - errorZ)


    yaw = round(gyroAngleZ)
    roll = round(gyroAngleX)
    pitch = round(gyroAngleY)

    angle0 = pitch
    angle1 = roll
    angle2 = yaw

    my_servo0.angle = angle0
    my_servo1.angle = angle1
    my_servo2.angle = angle2

    print(pitch, roll, yaw)
    time.sleep(0.05)
    #c
