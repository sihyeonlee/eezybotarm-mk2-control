import pygame
from func import serial_
from func import joystick_


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

past_list = [-1, -1, -1, -1]

while True:
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axes_list = []
            data_list = []

            for i in range(controller_info[2]):
                axes_list.append(round(controller.get_axis(i)))

            if axes_list[2] != 0:
                continue

            if past_list == axes_list:
                continue

            past_list = axes_list
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

        else:
            continue
