import unittest
import adafruit_minimqtt
import fake_socket as socket
import esp32spi

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_new_client(self):
        client = adafruit_minimqtt.MQTT(socket.Socket(), "127.0.0.1", esp=esp32spi.Interface())
        self.assertTrue(client)

    def test_open_connection(self):
        client = adafruit_minimqtt.MQTT(socket.Socket(), "127.0.0.1", esp=esp32spi.Interface())
        self.assertTrue(client.connect())

if __name__ == '__main__':
    unittest.main()
