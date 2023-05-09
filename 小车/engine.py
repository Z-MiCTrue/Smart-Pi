import RPi.GPIO as GPIO
import time


# 电机引脚初始化操作
def motor_init():
    # 小车电机引脚定义
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    ENA = 16
    ENB = 13
    # 设置GPIO口为BCM编码方式
    GPIO.setmode(GPIO.BCM)
    # 忽略警告信息
    GPIO.setwarnings(False)
    global pwm_ENA
    global pwm_ENB
    # global delaytime
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    # 设置pwm引脚和频率为2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def voltage_set(signal):
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    GPIO.output(IN1, signal[0])
    GPIO.output(IN2, signal[1])
    GPIO.output(IN3, signal[2])
    GPIO.output(IN4, signal[3])
    pass


# 小车停止
def brake(speed=100, delay_time=None):
    signal = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
    voltage_set(signal)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    if delay_time is not None:
        time.sleep(delay_time)
    else:
        pass


# rate: [offset(left-right+), float_speed, base_speed]
def flexible_run(rate, delay_time=None):
    signal = [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
    voltage_set(signal)
    pwm_ENA.ChangeDutyCycle(int((1 - rate[0]) * rate[1] / 2 + rate[2]))
    pwm_ENB.ChangeDutyCycle(int((1 + rate[0]) * rate[1] / 2 + rate[2]))
    if delay_time is not None:
        time.sleep(delay_time)
    else:
        pass
    brake()


# 小车前进
def forward(speed, delay_time=None):
    signal = [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
    voltage_set(signal)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    if delay_time is not None:
        time.sleep(delay_time)
    else:
        pass
    brake()


# 小车左转
def left(speed, delay_time=None):
    signal = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
    voltage_set(signal)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(speed)
    if delay_time is not None:
        time.sleep(delay_time)
    else:
        pass
    brake()


# 小车右转
def right(speed, delay_time=None):
    signal = [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW]
    voltage_set(signal)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(0)
    if delay_time is not None:
        time.sleep(delay_time)
    else:
        pass
    brake()


def GPIO_quit():
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    motor_init()
    forward(20, delay_time=1)
    right(20, delay_time=1.5)
    left(20, delay_time=3)
    pass
