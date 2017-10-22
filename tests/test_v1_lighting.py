import unittest
from lwrf.v1.light import Light
from lwrf.v1.hub import Hub


class TestV1Lighting(unittest.TestCase):

    def setUp(self):
        self.hub = Hub("127.0.0.1", 9760)
        self.room = 1
        self.device = 1
        self.light = Light(
            hub=self.hub,
            room_id=self.room,
            device_id=self.device
        )

    def test_light_brightness_is_not_more_than_32(self):
        set_state = self.light.change_state(state='DIM',
                                            brightness=33)
        self.assertEqual(set_state['return_code'], 1)

    def test_light_brightness_can_be_changed(self):
        set_state = self.light.change_state(state='DIM',
                                            brightness=16)
        self.assertEqual(set_state['return_code'], 0)

    def test_light_can_be_switched_on(self):
        set_state = self.light.change_state(state='ON')
        self.assertEqual(set_state['return_code'], 0)

    def test_light_can_be_switched_off(self):
        set_state = self.light.change_state(state='OFF')
        self.assertEqual(set_state['return_code'], 0)
