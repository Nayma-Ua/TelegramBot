from app import Basic

bot = Basic()

bot.require([
  ["modules.test", "Test"]
])

def start(data, api):
  if data["text"] == "/start":
    api.on("sendMessage", {"chat_id": data["chat"]["id"], "text": "Write /help to get information with me!"})

def help(data, api):
  if data["text"] == "/help":
    api.on("sendMessage", {"chat_id": data["chat"]["id"], "text": "This is help!\n My commands:\n /audio - send audio file\n /photo - send photo \n /file - send document"})

def audio(data, api):
  if data["text"] == "/audio":
    api.on("sendAudio", {"chat_id": data["chat"]["id"], "path": "files/audio.mp3"})

def photo(data, api):
  if data["text"] == "/photo":
    api.on("sendPhoto", {"chat_id": data["chat"]["id"], "path": "files/photo1.jpg"})

def file(data, api):
  if data["text"] == "/file":
    api.on("sendDocument", {"chat_id": data["chat"]["id"], "path": "files/file.txt"})

bot.add(start, help, audio, photo, file)
bot.start()