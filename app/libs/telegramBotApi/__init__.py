from requests import post, get

class Api:
  def __init__(self, token):
    self.api = 'https://api.telegram.org/bot%s/' % token

  def on(self, name, data={}):
    try:
      files = {}
      _type = False
      if   name == "sendPhoto":    _type = "photo"
      elif name == "sendAudio":    _type = "audio"
      elif name == "sendDocument": _type = "document"

      # send type
      if _type != False:
        if data.get("link") != None:    # send from the Internet
          linkFile = get(data["link"])
          nameFile = data["link"].split("/")[-1]
          files    = {_type: (nameFile, linkFile.content)}

        elif data.get("path") != None:  # send from the disk
          files    = {_type: open(data["path"], "rb")}

      request = post(self.api + name, data=data, files=files).json()
      if request["ok"] == False:
        self.log("[%s] %s" % (name, request["description"]))
        return False
      else:
        return request["result"]
    except:
      self.log("[%s] %s" % (name, request["description"]))
      return False

  def log(self, text):
    print("[TelegramBotApi] [log]", text)
    return False