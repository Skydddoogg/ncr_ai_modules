import speech_recognition as sr

def play():

    # Declare necessary variables
    r = sr.Recognizer()
    m = sr.Microphone()
    
    # Set up for microphone
    with m as source: r.adjust_for_ambient_noise(source)

    # Listern to microphone
    print("STT - Speak off!")
    with m as source: audio = r.listen(source)
    print("STT - Processing...")

    # Process STT
    try:

        # Recognize speech using Google Speech Recognition
        value = r.recognize_google(audio, language="th-TH")

        # Show result
        print("STT - You said {}".format(value))
        return value
    except sr.UnknownValueError:
        print("STT - Oops! Didn't catch that")
        return "0"
    except sr.RequestError as e:
        print("STT - Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        return "0"