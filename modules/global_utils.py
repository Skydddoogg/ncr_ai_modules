import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def show_module_log(message):
    print('%5s %s' % (' ', message))