from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


class FactoryLazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


if __name__ == '__main__':
    # conn = LazyConnection(('www.python.org', 80))  # Connection closed
    # with conn as s:
    #     # conn.__enter__()  # executes: connection open
    #     s.send(b'GET /index.html HTTP/1.0\r\n')
    #     s.send(b'Host: www.python.org\r\n')
    #     s.send(b'\r\n')
    #    # conn.__exit__()  # executes: connection closed
    #     resp = b''.join(iter(partial(s.recv, 8192), b''))

    conn = FactoryLazyConnection(('www.python.org', 80))
    with conn as s1:
        s1.send(b'GET /index.html HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
       # conn.__exit__()  # executes: connection closed
        resp = b''.join(iter(partial(s1.recv, 8192), b''))
        print(resp)
        with conn as s2:
            s2.send(b'GET /index.html HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            # conn.__exit__()  # executes: connection closed
            resp = b''.join(iter(partial(s2.recv, 8193), b''))
            print(resp)
