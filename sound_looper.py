# this script is an eternal soundfile looper. It plays all .wav and .mp3 files in a folder, and keeps looping the list
# code by Halfdan Hauch Jensen @AIR LAB ITU, halj@itu.dk

import pygame
import glob
import time

pygame.mixer.init()
time.sleep(10) # wait for the UDB drive to mount

playlist = list()
types = ('/media/air/AIR_DISK/*.wav', '/media/air/AIR_DISK/*.mp3')

for files in types: # compiles the directory file list
    playlist.extend(glob.glob(files))

playlist = sorted(playlist, key = lambda s: s.casefold()) # sorting the list in non case sensitive manner

for i in range(len(playlist)): # prints the list in nice formatted way
    print(playlist[i])

index = 0
running = True

while running: # eternal loop
    if not pygame.mixer.music.get_busy(): # sound stopped, time for next song
        pygame.mixer.music.load ( playlist[index] )
        pygame.mixer.music.play()
        index = index +1
        if index > len(playlist)-1:
            index = 0