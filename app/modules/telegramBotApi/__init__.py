from requests import post, get

class Api:
  def __init__( self, token ):
    self.api = 'https://api.telegram.org/bot%s/' % token

  def getMe( self ):
    try:
      request = post( self.api + "getMe" ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def getUpdates( self, offset=0, limit=10, timeout=0 ):
    try:
      data = {
        "offset": offset,
        "limit": limit,
        "timeout": timeout
      }
      request = post( self.api + "getUpdates", data=data ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendMessage( self, chat_id, text, reply_to_message_id=None, disable_web_page_preview=None, reply_markup=None ):
    try:
      data = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": disable_web_page_preview,
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": reply_markup
      }
      request = post( self.api + "sendMessage", data=data ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def forwardMessage(self, chat_id, from_chat_id, message_id):
    try:
      data = {
        "chat_id": chat_id,
        "from_chat_id": from_chat_id,
        "message_id": message_id
      }
      request = post(self.api + "forwardMessage", data=data).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendPhoto(self, chat_id, photo, reply_to_message_id=None, caption=None, reply_markup=None):
    try:
      data = {
        "chat_id": chat_id,
        "caption": caption,
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": reply_markup
      }
      request = post( self.api + "sendPhoto", data=data, files={'photo': open(photo, "rb")} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendAudio(self, chat_id, audio, reply_to_message_id=None, duration=None, reply_markup=None):
    try:
      data = {
        "chat_id": chat_id,
        "duration": duration,
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": reply_markup
      }
      request = post( self.api + "sendAudio", data=data, files={'audio': open(audio, "rb")} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendDocument(self, chat_id, document, reply_to_message_id=None):
    try:
      data = {
        "chat_id": chat_id,
        "reply_to_message_id": reply_to_message_id
      }
      request = post( self.api + "sendDocument", data=data, files={'document': open(document, "rb")} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendPhotoUrl(self, chat_id, link, reply_to_message_id=None):
    try:
      data = {
        "chat_id": chat_id,
        "reply_to_message_id": reply_to_message_id
      }
      img = get( link )
      request = post( self.api + "sendPhoto", data=data, files={"photo": ("image.png", img.content)} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendAudioUrl(self, chat_id, link, reply_to_message_id=None):
    try:
      data = {
        "chat_id": chat_id,
        "reply_to_message_id": reply_to_message_id
      }
      audio = get( link )
      request = post( self.api + "sendAudio", data=data, files={"audio": ("audio.mp3", audio.content)} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendDocumentUrl(self, chat_id, link, reply_to_message_id=None):
    try:
      data = {
        "chat_id": chat_id,
        "reply_to_message_id": reply_to_message_id
      }
      document = get( link )
      nameDocument = link.split("/")[-1]
      request = post( self.api + "sendDocument", data=data, files={"document": (nameDocument, document.content)} ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def sendSticker(self, chat_id, sticker, reply_to_message_id=None, reply_markup=None):
    try:
      data = {
        "chat_id": chat_id,
        "sticker": sticker,
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": reply_markup
      }
      request = post( self.api + "sendSticker" ).json()
      if request["ok"] == False:
        self.log( "[error] ok != true" )
      else:
        return request["result"]
    except:
      self.log( "[error] bad request" )

  def log( self, text ):
    print("[TelegramBotApi] [log]", text)




