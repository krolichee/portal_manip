from ev3dev2.control.webserver import motor_max_speed
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, Motor, MoveTank, SpeedPercent
from ev3dev2.motor import *
from ev3dev2._platform.ev3 import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

Y_AMP_MAX = 2200
X_AMP_MAX = 1300

ts_y = TouchSensor(INPUT_1)
ts_x = TouchSensor(INPUT_3)
m_y = MediumMotor(OUTPUT_A)
m_x1 = Motor(OUTPUT_B)
m_x2 = LargeMotor(OUTPUT_D)
mt_x = MoveTank(OUTPUT_B, OUTPUT_D)
mt_x.cs = ColorSensor(INPUT_2)

def new_function():
    pass
    pass

def home_y():
    m_y.run_forever(speed_sp=-300)
    ts_y.wait_for_pressed()
    m_y.stop()

def home_x():
    mt_x.run_forever(speed_sp=-300)
    ts_x.wait_for_pressed()
    mt_x.stop()

def test_x():
    mt_x.run_forever(speed_sp=100)
    ts_x.wait_for_released()

    try:
        while not ts_x.is_pressed:
            mt_x.follow_line( kp=11.3, ki=0.05, kd=3.2, speed=SpeedPercent(30),
                              follow_for=follow_for_forever,follow_left_edge=False,target_light_intensity=16,sleep_time=0.01,)
    except LineFollowErrorTooFast:
        mt_x.stop()
    mt_x.stop()


home_y()
m_y.speed_sp = 500
m_y.run_to_rel_pos(position_sp=Y_AMP_MAX/2)


