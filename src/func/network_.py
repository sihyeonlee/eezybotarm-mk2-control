import socket


def init():
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return soc


def send_data(soc, data_list, ip, port):
    data = bytearray()

    for i in data_list:
        b_i = bytes(i.encode())
        data.extend(b_i)

    soc.sendto(data, (ip, int(port)))

