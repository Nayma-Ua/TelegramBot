from flask import Flask, request
from json import loads, dumps
from app.modules.telegramBotApi import Api

class Bot:
  def __init__( self, ip, port, token, name ):
    self.ip = ip
    self.port = int( port )
    self.token = token
    self.name = name

    self.methods = ()

    self.API = Api(self.token)

  def include( self, *methods ):
    self.methods = methods

  def selectFunction( self ):
    try:
      upload = request.get_json(force=True)
      for method in self.methods:
        data = {
          "chat_id": upload["message"]["chat"]["id"],
          "user_id": upload["message"]["from"]["id"],
          "message_id": upload["message"]["message_id"],
          "message_text": upload["message"]["text"]
        }
        try:
          data["username"] = upload["message"]["from"]["username"]
        except:
          data["username"] = False
        try:
          data["last_name"] = upload["message"]["from"]["last_name"]
        except:
          data["last_name"] = False
        try:
          data["first_name"] = upload["message"]["from"]["first_name"]
        except:
          data["first_name"] = False

        method(data, self.API)
      return "Ok"
    except Exception as err:
      self.log("[error] %s" % err)
      return "Fail"

  def log( self, text ):
    print("[%s] [log] %s" % ( self.name, text ) )

  def start( self ):
    app = Flask(__name__)
    app.add_url_rule('/', view_func=self.selectFunction, methods=["GET", "POST"])
    app.run(host=self.ip, port=self.port)