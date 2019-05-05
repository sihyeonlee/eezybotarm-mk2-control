import socket


def init(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(('0.0.0.0', port))

    return soc


def send_data(soc, data_list, ip, port):
    data = bytearray()

    for i in data_list:
        b_i = bytes(i.encode())
        data.extend(b_i)

    soc.sendto(data, (ip, int(port)))

