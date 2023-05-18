import RPi.GPIO as GPIO

from MD_Ultrasonic import distance_measure
import engine as Engine


def detour():
    Engine.brake()


def auto_track(arg=None):
    # 初始设定
    TrackSensorLeftPin1 = 3  # 定义左边第一个循迹红外传感器引脚为3口
    TrackSensorLeftPin2 = 5  # 定义左边第二个循迹红外传感器引脚为5口
    TrackSensorRightPin1 = 4  # 定义右边第一个循迹红外传感器引脚为4口
    TrackSensorRightPin2 = 18  # 定义右边第二个循迹红外传感器引脚为18口
    GPIO.setup(TrackSensorLeftPin1, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2, GPIO.IN)
    GPIO.setup(TrackSensorRightPin1, GPIO.IN)
    GPIO.setup(TrackSensorRightPin2, GPIO.IN)
    TrackSensorLeftValue1 = GPIO.input(TrackSensorLeftPin1)
    TrackSensorLeftValue2 = GPIO.input(TrackSensorLeftPin2)
    TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
    TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)
    # 触线处理
    # 处理右锐角和右直角的转动
    if (TrackSensorLeftValue1 == False or TrackSensorLeftValue2 == False) and TrackSensorRightValue2 == False:
        Engine.right(30, None)
    # 处理左锐角和左直角的转动
    elif TrackSensorLeftValue1 == False and (TrackSensorRightValue1 == False or TrackSensorRightValue2 == False):
        Engine.left(30, None)
    # 最左边检测到
    elif TrackSensorLeftValue1 == False:
        Engine.left(30, None)
    # 最右边检测到
    elif TrackSensorRightValue2 == False:
        Engine.right(30, None)
    # 处理左小弯
    elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == True:
        Engine.left(35, None)
    # 处理右小弯
    elif TrackSensorLeftValue2 == True and TrackSensorRightValue1 == False:
        Engine.right(35, None)
    # 处理直线
    elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == False:
        Engine.forward(35, None)
    # 避障处理
    MD_C = distance_measure()
    if MD_C == -1:
        MD_C = distance_measure()
        if MD_C == -1:
            detour()


if __name__ == '__main__':
    Engine.motor_init()
    auto_track()
    Engine.brake()
    Engine.GPIO_quit()
