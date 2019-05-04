import socket


def init(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(('0.0.0.0', port))

    return soc


def send_data(soc, data, ip, port):
    soc.sendto(data, (ip, port))
