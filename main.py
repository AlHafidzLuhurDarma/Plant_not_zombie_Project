import pygame
import time
import serial


arduinoData = serial.Serial('com3', 9600)
tips = True
time.sleep(1) 

while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()  
    dataPacket=str(dataPacket,'utf-8')   
    dataPacket=dataPacket.strip('\r\n') 
    print(dataPacket)
    if tips == True:
        if dataPacket == "give me tips":
            pygame.mixer.init()
            pygame.mixer.music.load("Tips.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(1000)
            tips = False
    else:
        pass

