# kivy_textbutton_sample
## Source code for this youtube video: [https://youtu.be/hbSk3cM7T6Q](https://youtu.be/hbSk3cM7T6Q)

### I tested these with the following:

- Python 3.7** (On Linux Mint 20, PPA [here](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa))
- Kivy library: 1.11.1
- KivyMD: 0.104.1
- Kaki: 0.1.4

### Simply do the following (as user):

1) $ `sudo add-apt-repository ppa:deadsnakes/ppa`
2) $ `sudo apt-get update`
3) $ `sudo apt-get install python3.7-dev`
4) $ `python3.7 -m pip install https://github.com/kivy/kivy/archive/1.11.1.zip`
5) $ `python3.7 -m pip install https://github.com/kivymd/KivyMD/archive/0.104.1.zip`
6) $ `python3.7 -m pip install kaki`
7) $ `git clone https://github.com/Twilight0/kivy_textbutton_sample.git`
8) $ `cd kivy_textbutton_sample`
9) $ `DEBUG=1 python3.7 ./main.py`

** = Python3.8+ does not work with kivy 1.XX
