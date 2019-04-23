import pygame

pygame.init()                                           # Initialize Pygame Module
mod_pad = pygame.joystick
mod_pad.init()                                          # Initialize joystick func

if mod_pad.get_init() is 1:
    print("Initialize Success")
else:
    print("Failed Initialize")

pad_cnt = pygame.joystick.get_count()
print("Now", pad_cnt, "Devices Connect")

controller = mod_pad.Joystick(0)                        # Create a new Joystick object

controller.init()                                       # Initialize Controller

if controller.get_init() is 1:
    print("Controller Initialize Success")
else:
    print("Failed Controller Initialize")

print()
print("Controller Info")
print("===")
print("ID :", controller.get_id())
print("System Name :", controller.get_name())
print("Num Axes :", controller.get_numaxes())
print("Num Ball :", controller.get_numballs())
print("Num Button :", controller.get_numbuttons())
print("Num Hats :", controller.get_numhats())
print("===")

while True:
    pygame.event.pump()
    for i in range(controller.get_numaxes()):
        print("Axis %d value: %0.2f" % (i, float(controller.get_axis(i))))