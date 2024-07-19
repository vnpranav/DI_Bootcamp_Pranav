class Phone:
   def __init__(self, phone_number):
      self.phone_number = phone_number
      self.call_history = []
      self.messages  = []

   def call(self, other_phone):
      self.call_history.append(other_phone.phone_number)
      other_phone.call_history.append(self.phone_number)
      print(f"{self.phone_number} is calling {other_phone.phone_number}")

   def show_call_history(self):
      for call in self.call_history:
         print(call)

   def send_message(self, other_phone, content):
      message = {
         "to" : other_phone.phone_number,
         "from" : self.phone_number,
         "content" : content
      }

      self.messages.append(message)

   def show_incoming_messages(self):
      for message in self.messages:
         if message["to"] == self.phone_number:
            print(f"from : {message['from']} : {message['content']}")

   def show_outgoing_messages(self):
      for message in self.messages:
         if message["from"] == self.phone_number:
            print(f"to : {message['to']} : {message['content']}")

   def show_messages_from(self):
      for message in self.messages:
         if message["from"] == self.phone_number:
            print(f"from : {message['from']} : {message['content']}")
