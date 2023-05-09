import RPi.GPIO as GPIO
import time


def hear_init():
    # 基础设置
    EchoPin = 0
    TrigPin = 1
    GPIO.setmode(GPIO.BCM)  # 设置GPIO口为BCM编码方式
    GPIO.setwarnings(False)  # 忽略警告信息
    GPIO.setup(EchoPin, GPIO.IN)
    GPIO.setup(TrigPin, GPIO.OUT)


# 超声波函数
def distance_measure(arg=None):
    # 超声波引脚定义
    EchoPin = 0
    TrigPin = 1
    GPIO.output(TrigPin, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin, GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    distance = ((t2 - t1) * 340 / 2) * 100
    if distance <= 10:
        print('distance is: {}'.format(distance))
        return -1
    else:
        return distance
