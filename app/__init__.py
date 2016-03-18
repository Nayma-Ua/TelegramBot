from app.libs.telegramBotApi      import Api
from flask                        import Flask, request
from json                         import loads, dumps
from time                         import sleep
from importlib                    import import_module

class BotModel:
  def __init__(self, name, token):
    # Base data
    self.name = name
    self.token = token

    # Event methods
    self.methods = ()

    # Event modules
    self.modules = []

    # Api lib
    self.API = Api(self.token)

  def add(self, *methods):
    self.methods += methods

  def include(self, modules):
    self.modules += modules

  def runMethod(self, methods, update):
    data = {
      "chat_id": update["message"]["chat"]["id"],
      "user_id": update["message"]["from"]["id"],
      "message_id": update["message"]["message_id"]
    }
    if update["message"].get("text") != None:
      data["message_text"] = update["message"]["text"]
    else:
      data["message_text"] = ""

    if update["message"]["from"].get("username") != None:
      data["username"] = update["message"]["from"]["username"]
    else:
      data["username"] = "*user login*"

    if update["message"]["from"].get("last_name") != None:
      data["last_name"] = update["message"]["from"]["last_name"]
    else:
      data["last_name"] = "*user lastname*"

    if update["message"]["from"].get("first_name") != None:
      data["first_name"] = update["message"]["from"]["first_name"]
    else:
      data["first_name"] = "*user firstname*"

    for module in self.modules:
      if type(module) is str:
        includeModule = import_module(module)
        func = getattr(includeModule, "update")
        func(data, self.API)

      if type(module) is list:
        includeModule = import_module(module[0])
        _class = getattr(includeModule, module[1])
        objClass = _class(self.init)
        objClass.update(data, self.API)

    for method in methods:
      method(data, self.API)

  def log(self, text):
    print("[%s] [log] %s" % (self.name, text))


class Basic(BotModel):
  def __init__(self):
    # Load settings
    openInit = open("init.json", "r")
    self.init = loads(openInit.read())
    openInit.close()

    # Father run
    BotModel.__init__(self, self.init["bot_name"], self.init["access_token"])

    # Request data
    self.offset = 0
    self.limit = 10

  def checkUpdates(self):
    for update in self.API.getUpdates(self.offset, self.limit):
      self.offset = update["update_id"] + 1
      try:
        self.runMethod(self.methods, update)
      except Exception as err:
        self.log("[error] %s" % err)

  def start(self):
    while True:
      sleep(self.init["data"]["pause"])
      self.checkUpdates()


class Server(BotModel):
  def __init__(self):
    # Load settings
    openInit = open("init.json", "r")
    self.init = loads(openInit.read())
    openInit.close()

    # Father run
    BotModel.__init__(self, self.init["bot_name"], self.init["access_token"])

  def selectFunction(self):
    try:
      update = request.get_json(force=True)
      self.runMethod(self.methods, update)
    except Exception as err:
      self.log("[error] %s" % err)

  def start(self):
    app = Flask(__name__)
    app.add_url_rule('/', view_func=self.selectFunction, methods=["GET", "POST"])
    app.run(host=self.init["ip"], port=self.init["port"])