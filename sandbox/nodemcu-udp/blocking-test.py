import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('0.0.0.0', 828))
soc.setblocking(False)

data = 0

while True:
    try:
        data, addr = soc.recvfrom(1024)

    except OSError:
        print("non-blocking")

        pass

    print(data)
