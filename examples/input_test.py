from daemon.terminal.keyboard import Keyboard



while True:
    keyboard = Keyboard()
    key = keyboard.read()
    print(key)

