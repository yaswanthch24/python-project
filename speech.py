import speech_recognition as sr
git remote add origin https://github.com/yaswanthch24/python-project.git
git branch -M main
git push -u origin main
def main():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("please say something")

        audio =r.listen(source)

        print("Recognizing Now......")


        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n")


        except Exception as e:
            print("error : " +str(e))


        with open("recorder.wav","wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":
    main()
