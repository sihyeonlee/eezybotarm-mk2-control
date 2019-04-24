import machine
from machine import UART
import time

MAX_DUTY = 120
MIN_DUTY = 30
right_pin = 14
left_pin = 4
bottom_pin = 12


def init_servo(pin):
    servo = machine.PWM(machine.Pin(pin), freq=50)

    return servo


def init_uart(id, baud):
    uart = UART(id, baud)
    uart.init(baud, bits=8, parity=None, stop=1, timeout=15)

    return uart


right_servo = init_servo(right_pin)
left_servo = init_servo(left_pin)
bottom_servo = init_servo(bottom_pin)

right_servo.duty(100)
left_servo.duty(80)
bottom_servo.duty(70)

p_b = 70
p_l = 80
p_r = 100

uart = init_uart(0, 115200)

p_b_data = 'BN'
p_l_data = 'LN'
p_r_data = 'RN'

while True:
    data = uart.readline()

    if data == None:
        pass

    else:
        print(data)

        d_data = data.decode()
        b_data = d_data[0:2]
        l_data = d_data[2:4]
        r_data = d_data[4:6]

        p_b_data = b_data
        p_l_data = l_data
        p_r_data = r_data

    if p_b_data == 'BU' and p_b < 130:
        n_b = p_b + 1
    elif p_b_data == 'BD' and p_b > MIN_DUTY:
        n_b = p_b - 1
    else:
        n_b = p_b

    if p_l_data == 'LU' and p_l < MAX_DUTY:
        n_l = p_l + 1
    elif p_l_data == 'LD' and p_l > 60:
        n_l = p_l - 1
    else:
        n_l = p_l

    if p_r_data == 'RU' and p_r < MAX_DUTY:
        n_r = p_r + 1
    elif p_r_data == 'RD' and p_r > 80:
        n_r = p_r - 1
    else:
        n_r = p_r

    if n_b != p_b or n_l != p_l or n_r != p_r:
        right_servo.duty(n_r)
        left_servo.duty(n_l)
        bottom_servo.duty(n_b)

        print("Bottom Position :", n_b)
        print("Right Position :", n_r)
        print("Left Postion :", n_l)

        p_b = n_b
        p_r = n_r
        p_l = n_l

    time.sleep_ms(20)
