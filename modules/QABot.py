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
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation', # บอกผลลัพธ์ บวก ลบ คูณ และหาร
                'chatterbot.logic.BestMatch',
                'modules.ResourceQABot.CustomAdapters.GoogleSearchAdapter' # ค้นหาจาก Google ตาม Keyword
            ],
        )
        self.trainer = None

    def train(self):

        self.trainer = ChatterBotCorpusTrainer(self.chatbot_obj)

        self.trainer.train(
            os.path.join(global_utils.ROOT_DIR, 'ResourceQABot', 'data', 'english')
        )

        return self

    def get_response_text(self, incoming_text):
        response = self.chatbot_obj.get_response(incoming_text).text
        global_utils.show_module_log('QABot - ' + response)
        return response

    def play(self):

        if self.trainer == None:
            self.train()

        while True:
            text=input("Text: ")
            if text=="exit":
                break
            response = self.get_response_text(text)
            print(response)