# Healthy Programmer

# Job hours - 9am to 5pm
# Water - water.mp3 (3.5 liters) ( 200ml Glass) - Drank input to stop the mp3 - log
# Eyes - eyes.mp3 - every 30 min - Eydone - log
# Physical activity - physical.mp3 every - 45 min and to stop Ex done - log

# Rules -
#pygame module to play audio

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
















