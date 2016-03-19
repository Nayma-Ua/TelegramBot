from json import dumps

def visualKeyboard(keyboard, resize_keyboard = False, one_time_keyboard = True, selective = False):
  reply_markup = {
      'keyboard': keyboard,
      'resize_keyboard': resize_keyboard,
      'one_time_keyboard': one_time_keyboard,
      'selective': selective
  }
  return dumps(reply_markup)

def multiCommand(data, command):
  if data == command:
    return True
  elif data.split("@")[0] == command:
    return True
  else:
    return False