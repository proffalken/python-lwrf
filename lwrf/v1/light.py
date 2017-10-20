# import lwrf.v1.sender
import socket


class Light():

    def __init__(
            self,
            device_id=0,
            room_id=0,
            state="OFF",
            brightness=32):
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
        # self.hub.send_message(self.message.encode())
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        sock.sendto(self.message.encode(), ("10.224.231.124", 9760))

    def _switch_off(self):
        self.message = ",!%s%sF0" % (
            self.room_id,
            self.device_id
        )
        # self.hub.send_message(self.message.encode())
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        sock.sendto(self.message.encode(), ("10.224.231.124", 9760))

    def _set_brightness(self, brightness):
        self.message = ",!%s%sFdP%s" % (
            self.room_id,
            self.device_id,
            brightness
        )
        # self.hub.send_message(self.message.encode())
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        sock.sendto(self.message.encode(), ("10.224.231.124", 9760))

    def change_state(self, state="OFF", brightness=0):
        _msg = "State Change Failed"
        _return_code = 128
        if state == "OFF":
            self._switch_off()
            _msg = "OFF Instruction Sent"
            _return_code = 0
        elif state == "ON":
            self._switch_on()
            _msg = "ON Instruction Sent"
            _return_code = 0
        elif state == "DIM":
            if brightness > 32:
                _msg = """
Lightwave supports values between 0 (OFF) and 32 (100%) for brightness.
"""
                _return_code = 1
            else:
                _msg = "Brightness Changed to %s%%" % (brightness / 32 * 100)
                _return_code = 0
            self._set_brightness(brightness)
        _ret_obj = {
            'message': _msg,
            'return_code': _return_code
        }
        return _ret_obj
