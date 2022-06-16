import pygame
import time

time.sleep(10) # wait for the UDB drive to mount

pygame.mixer.init()
#pygame.mixer.music.load("sound.wav")
pygame.mixer.music.load("/media/air/AIR_DISK1/sound.wav")
pygame.mixer.music.play(-1) # note -1 for playing in loops
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
    

# https://stackoverflow.com/questions/62853263/pygame-sound-when-started-from-terminal-not-from-nodered

# https://www.instructables.com/Syncing-Folders-With-Python/
