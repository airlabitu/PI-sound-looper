# PI-sound-looper

Loops an .wav audio file on a Raspberry Pi using Python and autostart

## INSTALL PYTHON MODULES

Make sure you have the following two modules. They should be preinstalled with the Raspberry Pi OS.
**time**
**pygame**



## ADD SOUND_LOOPER
Place a copy of the Python file **sound_looper.py** in the home directory

e.g. **/home/"usernme"/** - in my case **/home/air/** or if you are using the standard username then it is **/home/pi/**

Open the script and correct the path name to reflect your username. It should now be called something like:
```/media/YOUR_USERNAME/AIR_DISK/sound.wav```


## AUTOSTART AT BOOT
Type the following in a terminal window to open the autostart text file
```sudo nano /etc/xdg/lxsession/LXDE-pi/autostart```

add this line in the end of the autostart document
```@python /home/air/sound_looper.py``` (correct if you changed the username)

press **ctrl+x** to exit followed by **shift+y** to save.


## SETUP SOUND DEVICE
open a terminal window and type
```sudo raspi-config``` to open the system settings

choose **System options** followed by **Audio**. 
Then choose the sound device you would like the audio to use. In our case we are using a USB sound interface, it is called **USB Audio** in the list.


## ADD USB DRIVE
Make sure you have inserted a USB drive named **AIR_DISK**, and that it has a soundfile called "sound.wav" in the root directory.


## REBOOT
Reboot the Pi, and wait for the sound to play


## DONE :-)


## IF THERE IS NO SOUND... WHAT COULD BE WRONG???
Try to take a look at the USB drive location with the Terminal app (command: ls ```/media/"username"/```) to see if it matches the path name given in the **sound_looper.py** script.
If not correct the path name in the script according to your system setup.

You will always need to alter the path name if you uesd another username than me (**air**).
