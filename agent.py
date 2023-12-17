class Agent:
  def __init__(self, name, system_message, model, max_iter):
    self.name = name
    self.model = model
    self.system_message = system_message
    self.max_iter = max_iter
    self.history = ""
    self.history = self.history + "\"text\":" + system_message + "\"role\":\"user\""

  def __generate__(self, messages):

    if self.name=="user":
        inp = input("Waiting for user input")
        return inp
    else :
        return self.model.generate_content(messages)

  def _start_(self, prompt):

    self.history = self.history + "\"text\":" + prompt + "\"role\":\"user\""

    for i in range(self.max_iter):
      response = self.__generate__(self.history)
      self.history = self.history + "\"text\":" + response + "\"role\":\"model\""
      print(response.text)
      inp = input("Waiting for user input:")
      if "exit" in inp:
        return
      else:
        self.history = self.history + "\"text\":" + inp + "\"role\":\"user\""
