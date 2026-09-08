from daemon.terminal.input import Input
from daemon.terminal.keys import Key



while True:
    key = Input.read()
    print(repr(key))

    if key == Key.ESC:
        print("Bye")
        break
