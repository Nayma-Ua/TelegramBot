from app.modules.telegramBotApi import Api
from time                       import sleep
class Bot:
  def __init__( self, name, token ):
    # Bot data
    self.name = name
    self.token = token

    # Modules
    self.API = Api(self.token)

    # Request data
    self.offset = 0
    self.limit = 10

  def include( self, *methods ):
    self.methods = methods

  def start( self, pause=0 ):
    while True:
      sleep(pause)
      self.checkUpdates()

  def checkUpdates( self ):
    for update in self.API.getUpdates( self.offset, self.limit ):
      self.offset = update["update_id"] + 1
      try:
        for method in self.methods:
          data = {
            "chat_id": update["message"]["chat"]["id"],
            "user_id": update["message"]["from"]["id"],
            "message_id": update["message"]["message_id"],
            "message_text": update["message"]["text"]
          }
          try:
            data["username"] = update["message"]["from"]["username"]
          except:
            data["username"] = ""
          try:
            data["last_name"] = update["message"]["from"]["last_name"]
          except:
            data["last_name"] = ""
          try:
            data["first_name"] = update["message"]["from"]["first_name"]
          except:
            data["first_name"] = ""

          method(data, self.API)
      except Exception as err:
        self.log("[error] %s" % err)


  def log( self, text ):
    print("[%s] [log] %s" % ( self.name, text ) )