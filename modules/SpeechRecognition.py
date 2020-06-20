import speech_recognition as sr

def play():

    print("โมดูล Speech-to-Text เริ่มทำงาน -------------------")

    # Declare necessary variables
    r = sr.Recognizer()
    m = sr.Microphone()
    
    # Set up for microphone
    with m as source: r.adjust_for_ambient_noise(source)

    # Listern to microphone
    print("พูดออกมาเลยค่ะ")
    with m as source: audio = r.listen(source)
    print("สักครู่น่ะค่ะ เรากำลังประมวลผลค่ะ...")

    # Process STT
    try:
        # Recognize speech using Google Speech Recognition
        value = r.recognize_google(audio, language="th-TH")

        # Show result
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print(u"คุณพูดว่า {}".format(value).encode("utf-8"))
            return value
        else:  # this version of Python uses unicode for strings (Python 3+)
            print("คุณพูดว่า {}".format(value))
            return value
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
        return "0"
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        return "0"