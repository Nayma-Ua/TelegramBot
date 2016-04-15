class Test:
  def __init__(self, data):
    self.data = data
    print("Module 'Test': request pause ->", self.data["pause"])

  def update(self, data, api):
    print("Module 'Test': message text ->", data["text"]) 