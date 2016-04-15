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
    self.objModules = ()

    # Api lib
    self.API = Api(self.token)

  def add(self, *data, _type="method"):
    if _type == "method": self.methods += data
    if _type == "module": self.objModules += data

  def require(self, modules):
    self.modules += modules

  def loadModules(self):
    for module in self.modules:
      includeModule = import_module(module[0])
      _class = getattr(includeModule, module[1])
      objClass = _class(self.init["data"])
      self.add(objClass, _type="module")

  def runMethod(self, methods, update):
    for module in self.objModules:
      module.update(update, self.API)

    for method in methods:
      method(update, self.API)

  def log(self, text):
    print("[%s] [log] %s" % (self.name, text))


class Basic(BotModel):
  def __init__(self):
    # Load settings
    openInit = open("manifest.json", "r", encoding="utf-8")
    self.init = loads(openInit.read())
    openInit.close()

    # Father run
    BotModel.__init__(self, self.init["bot_name"], self.init["access_token"])

    # Request data
    self.offset = 0
    self.limit = 10

  def checkUpdates(self):
    for update in self.API.on("getUpdates", {"offset": self.offset, "limit": self.limit}):
      self.offset = update["update_id"] + 1
      try:
        self.runMethod(self.methods, update["message"])
      except Exception as err:
        self.log("[error] %s" % err)

  def start(self):
    self.loadModules()
    while True:
      sleep(self.init["data"]["pause"])
      self.checkUpdates()


class Server(BotModel):
  def __init__(self):
    # Load settings
    openInit = open("manifest.json", "r", encoding="utf-8")
    self.init = loads(openInit.read())
    openInit.close()

    # Father run
    BotModel.__init__(self, self.init["bot_name"], self.init["access_token"])

  def selectFunction(self):
    try:
      update = request.get_json(force=True)
      self.runMethod(self.methods, update["message"])
    except Exception as err:
      self.log("[error] %s" % err)

  def start(self):
    self.loadModules()
    app = Flask(__name__)
    app.add_url_rule('/', view_func=self.selectFunction, methods=["GET", "POST"])
    app.run(host=self.init["ip"], port=self.init["port"])