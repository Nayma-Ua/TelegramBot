from app import Basic
bot = Basic()

bot.include([
  "modules.test",
  ["modules.test", "Test"]
])

def start(data, api):
  if data["message_text"] == "/start":
    api.sendMessage(data["chat_id"], "Write /help to get information with me!")

def help(data, api):
  if data["message_text"] == "/help":
    api.sendMessage(data["chat_id"], "This is help!\n My commands:\n /audio - send audio file\n /photo - send photo \n /file - send document")

def audio(data, api):
  if data["message_text"] == "/audio":
    api.sendAudio(data["chat_id"], "files/audio.mp3")

def photo(data, api):
  if data["message_text"] == "/photo":
    api.sendPhoto(data["chat_id"], "files/photo.jpg")

def file(data, api):
  if data["message_text"] == "/file":
    api.sendDocument(data["chat_id"], "files/file.txt")

bot.add(start, help, audio, photo, file)
bot.start()