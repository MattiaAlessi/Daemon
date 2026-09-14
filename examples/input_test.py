from daemon.input.keyboard import Keyboard



while True:
    keyboard = Keyboard()
    key = keyboard.read()
    print(key)

