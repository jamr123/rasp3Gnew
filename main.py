from time import sleep
import ioLecturas
import signal
import sys

IO=ioLecturas.Data()


def signal_handler(sig, frame):
    IO.cleanUp()
    sys.exit(1)

while True:

    signal.signal(signal.SIGINT, signal_handler)
    
    IO.crearReporte()
    print(IO.countCaudal1)
    print(IO.countCaudal2)
    sleep(1)