import machine
from machine import UART
import time

MAX_DUTY = 120
MIN_DUTY = 40

def init_servo(pin):
    servo = machine.PWM(machine.Pin(pin), freq=50)

    return servo

def init_uart(id, baud):
    uart = UART(id, baud)
    uart.init(baud, bits=8, parity=None, stop=1, timeout=1023)

    return uart


right_pin = 14
left_pin = 4
bottom_pin = 12

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

print("TEST")

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

    if p_b_data == 'BU':
        if p_b < MAX_DUTY:
            p_b = p_b + 5
    elif p_b_data == 'BD':
        if p_b > MIN_DUTY:
            p_b = p_b - 5
    elif p_b_data == 'BN':
        p_b = p_b

    if p_l_data == 'LU':
        if p_l < MAX_DUTY:
            p_l = p_l + 5
    elif p_l_data == 'LD':
        if p_l > MIN_DUTY:
            p_l = p_l - 5
    elif p_l_data == 'LN':
        p_l = p_l

    if p_r_data == 'RU':
        if p_r < MAX_DUTY:
            p_r = p_r + 5
    elif p_r_data == 'RD':
        if p_r > MIN_DUTY:
            p_r = p_r - 5
    elif p_r_data == 'RN':
        p_r = p_r

    right_servo.duty(p_r)
    left_servo.duty(p_l)
    bottom_servo.duty(p_b)