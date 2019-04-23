from machine import UART


def init_UART(id, baud):
    uart = UART(id, baud)
    uart.init(115200, bits=8)
    return uart


def deinit(uart):
    uart.deinit()