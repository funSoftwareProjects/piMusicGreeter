#!/usr/bin/python3
import subprocess
from pydub.playback import play
from pydub import AudioSegment
import time


def checkIfArrived(ip):
    output = ""
    try:
        output = subprocess.check_output(['ping', ip, '-c 1', '-w 2']).decode("utf-8")
    except subprocess.CalledProcessError as error:
        print(error)
    
    if "0% packet loss" in output:
        return True
    return False

def doublecheckIfArrived(ip):
    output = ""
    try:
        output = subprocess.check_output(['ping', ip, '-c 5', '-w 5']).decode("utf-8")
    except subprocess.CalledProcessError as error:
        print(error)
        print("Returning false")
        return False
    print(output)
    if "100% packet loss" not in output:
        print("Reutrning true")
        return True


class Person:
    ip = 0
    home = True
    song = ""
    arrived = ""
    gone = ""

def mainPart(input):
    if input.home == False:
        if checkIfArrived(input.ip) == True:
            print(str(input) + " has arrived")
            play(AudioSegment.from_mp3("announcing.mp3"))
            play(AudioSegment.from_mp3(input.arrived))
            play(AudioSegment.from_mp3(input.song))
            input.home = True    
    elif input.home == True and checkIfArrived(input.ip) == False:
        if doublecheckIfArrived(input.ip) == False:
            input.home = False
            play(AudioSegment.from_mp3("announcing.mp3"))
            print(str(input) + " has left")
            play(AudioSegment.from_mp3(input.gone))

startup_sound = AudioSegment.from_mp3("bootup.mp3")
play(startup_sound)


person1 = Person()
person1.ip = "192.168.1.12"
person1.song = ""
person1.arrivalSong = ""

while(1):
    print("Start of one iteration")
    mainPart(person1)
    time.sleep(1)
