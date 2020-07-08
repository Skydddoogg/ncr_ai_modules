from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from modules import global_utils
import pickle

class SimpleQABot(object):
    def __init__(self, bot_name):
        super(SimpleQABot, self).__init__()

        self.bot_name = bot_name
        self.chatbot_obj = ChatBot(
            self.bot_name,
            # storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
            # database = self.bot_name + '.sqlite3'
        )
        self.trainer = None

    def train(self):

        self.trainer = ChatterBotCorpusTrainer(self.chatbot_obj)

        self.trainer.train(
            os.path.join(global_utils.ROOT_DIR, 'ResourceQABot', 'corpus')
        )

        return self

    def get_response_text(self, incoming_text):

        return self.chatbot_obj.get_response(incoming_text)

    def play(self):

        if self.trainer == None:
            self.train()

        while True:
            text=input("Text: ")
            if text=="exit":
                break
            response = self.get_response_text(text)
            print(response)