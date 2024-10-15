import os

if __name__ == "__main__":
    print("Welcome to Robospeaker 1.1")
    while True:
        x = input("Write what you want to pronounce: ")
        if x.lower() == "q":
            os.system('powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye bye friend\');"')
            break
        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
        os.system(command)
