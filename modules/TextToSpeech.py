from gtts import gTTS
import playsound
import os
from modules.ResourceTextToSpeech import config

def play(text = None, remove_result = True, self_input = False):

    print("โมดูล Text-to-Speech เริ่มทำงาน -------------------")

    if self_input:
        text = input('\nคุณต้องการให้ฉันพูดว่าอะไร: ')

    # Convert text to speech
    tts = gTTS(text=text, lang='th')

    # Save result
    if not os.path.isdir(config.result_folder):
        os.mkdir(config.result_folder)
    result_path = os.path.join(config.result_folder, 'speech_result.mp3')
    tts.save(result_path)

    # Play result
    playsound.playsound(result_path, True)

    if remove_result:
        # Remove result file
        os.system('rm ' + result_path)