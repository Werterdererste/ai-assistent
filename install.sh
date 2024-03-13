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

read -p "Do you want to proceed? (y/n) " answer

if [ "$answer" = "y" ]; then
    /usr/bin/echo "Starting Install"

    /usr/bin/apt update
    /usr/bin/apt upgrade -y

    # install or update ollama
    /usr/bin/curl https://ollama.ai/install.sh | /bin/sh
    /usr/bin/systemctl start ollama.service
    /usr/local/bin/ollama pull tinyllama:1.1b

  # test to speach
    /usr/bin/apt install python3-pyaudio portaudio19-dev -y
  # speach to text
    /usr/bin/apt install flac libespeak1 -y
# sudo apt install espeak ffmpeg libespeak1 libespeak-dev

  # virtual environment installer, create and activate
    /usr/bin/apt install virtualenv -y
    virtualenv venv
    source venv/bin/activate

  # install components
    pip install -r requirements.txt
    pip install git+https://github.com/openai/whisper.git soundfile


elif [ "$answer" = "n" ]; then
    /usr/bin/echo "Don't install"
    exit 1
else
    /usr/bin/echo "Invalid response. Please answer with 'yes' or 'no'."
fi
