import socket


class Hub():

    def __init__(
            self,
            lwrf_host="127.0.0.1",
            port=9760):
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        self.host = lwrf_host
        self.port = port
        self.target = (self.host, self.port)

    def link_hub(self):
        link_msg = '!F*p'
        self.send_message(link_msg.encode())

    def send_message(self, message):
        self.sock.sendto(
            message.encode(),
            self.target
        )
