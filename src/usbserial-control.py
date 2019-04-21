import pygame
import serial_
import joystick_


pygame.init()

joystick = pygame.joystick
joystick_.init(joystick)

num_joystick = joystick.get_count()
if num_joystick < 0:
    print("Not Find Device")
else:
    print("Now %d Devices Connect" % num_joystick)

controller = joystick.Joystick(0)
joystick_.init(controller)

controller_info = joystick_.get_info(controller)

robot_arm = serial_.link("COM9", 115200)

while True:
    pygame.event.pump()

    axes_list = []
    data_list = []

    for i in range(controller_info[2]):
        axes_list.append(round(controller.get_axis(i)))

    print(axes_list)

    if axes_list[0] == 1:
        data_list.append('BU')
    elif axes_list[0] == -1:
        data_list.append('BD')
    else:
        data_list.append('BN')
    if axes_list[1] == 1:
        data_list.append('LD')
    elif axes_list[1] == -1:
        data_list.append('LU')
    else:
        data_list.append('LN')
    if axes_list[3] == 1:
        data_list.append('RD')
    elif axes_list[3] == -1:
        data_list.append('RU')
    else:
        data_list.append('RN')

    print(data_list)

    print(serial_.transmit_data_list(robot_arm, data_list))
