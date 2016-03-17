from app.reqBot import Bot
bot = Bot(name="BotHelper", token="")

@bot.include
def start(data, api):
  if data["message_text"] == "/start":
    api.sendMessage(data["chat_id"], "Write /help to get information with me!")

@bot.include
def help(data, api):
  if data["message_text"] == "/help":
    api.sendMessage(data["chat_id"], "This is help!\n My commands:\n /audio - send audio file\n /photo - send photo \n /file - send document")

@bot.include
def audio(data, api):
  if data["message_text"] == "/audio":
    api.sendAudio(data["chat_id"], "files/audio.mp3")

@bot.include
def photo(data, api):
  if data["message_text"] == "/photo":
    api.sendPhoto(data["chat_id"], "files/photo.jpg")

@bot.include
def file(data, api):
  print(data)
  if data["message_text"] == "/file":
    api.sendDocument(data["chat_id"], "files/file.txt")

bot.start()