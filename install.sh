#!/bin/bash
# run this file to install the components needed for this project
# for a raspberry pi

# Ensure script is being run as root
if [[ $(id -u) -ne 0 ]]; then
    /usr/bin/echo "This script must be run as root" >&2
    exit 1
fi

/usr/bin/echo This is script is made for Raspberry Pi os it should also works on other debian based systems.
/usr/bin/echo no guarantee that is does.
/usr/bin/echo on other systems IT DONT WORK

/usr/bin/read -p "Do you want to proceed? (y/n) " answer

if [ "$answer" = "y" ]; then
    /usr/bin/echo "Starting Install"

    /usr/bin/apt update
    /usr/bin/apt upgrade -y

    # install or update ollama
    /usr/bin/curl https://ollama.ai/install.sh | /bin/sh
    /usr/local/bin/ollama pull tinyllama:1.1b

    # virtuelle umgebung insallieren
   /usr/bin/apt install virtualenv

  # test to soeach
    /usr/bin/apt install python3-pyaudio
    /usr/bin/apt install portaudio19-dev


    /usr/bin/apt install flac
# sudo apt install espeak ffmpeg libespeak1 libespeak-dev

  virtual venv


elif [ "$answer" = "n" ]; then
    /usr/bin/echo "Don't install"
    exit 1
else
    /usr/bin/echo "Invalid response. Please answer with 'yes' or 'no'."
fi







## notes

# for text to speach

# sudo apt install espeak
# pip install pyttsx3
# sudo apt install libespeak-de
# sudo apt-get install alsa-utils

# for speach to text

# to this moment do nothing because i don't now what i need on the pi

