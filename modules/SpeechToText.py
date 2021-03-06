import speech_recognition as sr
from modules import global_utils

class SpeechToText(object):
    def __init__(self):
        super(SpeechToText, self).__init__()

    @staticmethod
    def play(return_value = False, language = 'en-EN'):

        print("Speech-To-Text (STT) is started")

        # Declare necessary variables
        r = sr.Recognizer()
        m = sr.Microphone()
        
        # Set up for microphone
        with m as source: r.adjust_for_ambient_noise(source)

        while True:
            # Listern to microphone
            global_utils.show_module_log("STT - Speak off!")
            with m as source: audio = r.listen(source)
            global_utils.show_module_log("STT - Processing...")

            # Process STT
            try:
                # Recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, language=language)

                # Show result
                global_utils.show_module_log("STT - You said {}".format(value))
                if return_value:
                    return value

            except sr.UnknownValueError:
                global_utils.show_module_log("STT - Oops! Didn't catch that")
                if return_value:
                    return "0"
            except sr.RequestError as e:
                global_utils.show_module_log("STT - Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                if return_value:
                    return "0"