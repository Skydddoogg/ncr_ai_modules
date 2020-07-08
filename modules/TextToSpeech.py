from gtts import gTTS
import os
from modules.ResourceTextToSpeech import config
import pygame

pygame.mixer.init()

def play(text = None, remove_result = True, self_input = False, repeat = True, language = 'en'):

    print("Text-To-Speech (TTS) is started")

    while True:

        if self_input:
            message = 'TTS - Enter what you want me to say: '
            text = input('%5s %s' % (' ', message))

        # Convert text to speech
        tts = gTTS(text=text, lang=language)

        # Save result
        if not os.path.isdir(config.result_folder):
            os.mkdir(config.result_folder)
        result_path = os.path.join(config.result_folder, 'speech_result.mp3')
        tts.save(result_path)

        # Play result
        # playsound.playsound(result_path, True)
        pygame.mixer.music.load(result_path)
        pygame.mixer.music.play()

        if remove_result:
            # Remove result file
            os.system('rm ' + result_path)

        if not repeat:
            return 0