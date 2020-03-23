import speech_recognition as sr

r = sr.Recognizer()

f = open("/home/burak/PycharmProjects/sesDeneme/sesKomutu.txt", "a", 0)

while True:
    with sr.Microphone() as source:
        print("Speak Anything :")
        a = r.listen(source, None, 3)
        try:
            text = r.recognize_google(a, None, "tr-TR")
            print text
            if(text == "buraya gel" or text == "gel" ):
                f.write("come")
            elif(text == "geri git" or text == "git" ):
                f.write("go")
            elif(text == "dur"):
                f.write("stop")
            elif(text == "sola"):
                f.write("turn around")
        except:
            print("Sorry could not recognize what you said")