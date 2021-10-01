#!/usr/bin/python3
import subprocess
from pydub.playback import play
from pydub import AudioSegment
import time

class Person:
    ip = 0
    home = True
    song = ""
    arrivalAnnouncement = ""
    departureAnnouncement = ""

person1 = Person()
person1.ip = "192.168.1.135"
person1.song = ""
person1.arrivalSong = ""



person2 = Person()
person2.ip = "192.168.1.135"
person2.song = ""
person2.arrivalSong = ""

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

def updateStatus(input):
    if input.home == False:
        if checkIfArrived(input.ip) == True:
            print(str(input) + " has arrived")
            play(AudioSegment.from_mp3("announcing.mp3"))
            play(AudioSegment.from_mp3(input.arrivalAnnouncement))
            play(AudioSegment.from_mp3(input.song))
            input.home = True    
    elif input.home == True and checkIfArrived(input.ip) == False:
        if doublecheckIfArrived(input.ip) == False:
            input.home = False
            play(AudioSegment.from_mp3("announcing.mp3"))
            print(str(input) + " has left")
            play(AudioSegment.from_mp3(input.departureAnnouncement))

startup_sound = AudioSegment.from_mp3("bootup.mp3")
play(startup_sound)


while(1):
    print("Start of one iteration")
    updateStatus(person1)
    updateStatus(person2)
    time.sleep(1)
