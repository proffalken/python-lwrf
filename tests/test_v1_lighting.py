import unittest
from lwrf.v1.light import Light


class TestV1Lighting(unittest.TestCase):

    def setUp(self):
        self.room = 1
        self.device = 1

    def test_light_device_can_be_created(self):
        self.light = Light(
            room_id=self.room,
            device_id=self.device
        )
