class Socket:
    def __init__(self):
        pass

    def set_interface(self, iface):
        pass

    def write(self, bytes):
        return len(bytes)

    def read(self, bytes):
        return b""

    def settimeout(self, timeout):
        pass

    def getaddrinfo(self, a, b):
        return (("", ""), "", "")

    def socket(self):
        return self

    def connect(self, addr, mode):
        pass
