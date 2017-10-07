import unittest
from lwrf import *


class TestV1Lighting(unittest.TestCase):

    def __setUp__(self):
        self.room = 1
        self.device = 1

    def test_light_device_can_be_created(self):
        self.light = lwrf.v1.light(room, device)
