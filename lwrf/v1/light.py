#import lwrf.v1.sender
import socket


class Light():

    def __init__(self,
            device_id = 0,
            room_id = 0,
            state = "OFF",
            brightness = 32):
        self.device_id = device_id
        self.room_id = room_id
        self.state = state
        self.brightness = brightness
        self.message = ''

    def _switch_on(self):
        self.message = ",!%s%sF1" % (
                self.room_id,
                self.device_id
                )
        #self.hub.send_message(self.message.encode())
        sock = socket.socket(socket.AF_INET, # Internet
                                     socket.SOCK_DGRAM) # UDP
        sock.sendto(self.message.encode(), ("10.224.231.124", 9760))

    def _switch_off(self):
        self.message = ",!%s%sF0" % (
                self.room_id,
                self.device_id
                )
        #self.hub.send_message(self.message.encode())
        sock = socket.socket(socket.AF_INET, # Internet
                                     socket.SOCK_DGRAM) # UDP
        sock.sendto(self.message.encode(), ("10.224.231.124", 9760))

    def change_state(self, state):
        if state == "OFF":
            self._switch_off()
        elif state == "ON":
            self._switch_on()
