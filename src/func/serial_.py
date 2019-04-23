import serial


def link(port, baud):
    return serial.Serial(port, baud)

def transmit_data_list(link_, data_list):
    data = bytearray()

    for i in data_list:
        b_i = bytes(i.encode())
        data.extend(b_i)

    data.extend(b'\n')

    link_.write(data)

    return data


def trasmit_data(link_, data):
    link_.write(data.encode())
