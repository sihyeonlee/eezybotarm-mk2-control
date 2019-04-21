import pygame


def init(object):
    object.init()

    if object.get_init() is 1:
        print("INIT : PASS")

        return True

    else:
        print("INIT : FAIL")

        return False


def get_info(controller):
    id = controller.get_id()
    name = controller.get_name()
    num_axes = controller.get_numaxes()
    num_ball = controller.get_numballs()
    num_button = controller.get_numbuttons()
    num_hats = controller.get_numhats()

    info_list = [id, name, num_axes, num_ball, num_button, num_hats]

    return info_list
