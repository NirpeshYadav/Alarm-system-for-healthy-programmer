# Alarm-system-for-healthy-programmer
#Created using Python...
#It play's alarm to notify user to take a break 

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log(data):
    with open("Log_Data.txt", "a") as f:
        f.write(f"{data}, {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 5
    eyesecs = 10
    exercisesecs = 15

    while True:
        if time() - init_water > watersecs:
            print("It's time to drink water and press drank stop the alarm")
            musiconloop("water.mp3.mp3" , "drank")
            init_water = time()
            log("Drank water at")

        if time() - init_eyes > eyesecs:
            print("It's time to take eyes break and press done to stop the alarm")
            musiconloop("eyes.mp3" , "done")
            init_eyes = time()
            log("Took eyes break at")

        if time() - init_exercise > exercisesecs:
            print("It's time to take break for exercise and press done to stop the alarm")
            musiconloop("exercise.mp3" , "stop")
            init_eyes = time()
            log("Done physical exercise at")
