# DyslexHelp

## About DyslexHelp
It has been observed that people with dyslexia are extremely smart but face small issues in recognising words. They face difficulty in mapping letters to their sounds. They also have difficulty in reading handwritten letters. This leads to anxiety in kids and also affects their mental health. DyslexHelp is an application to tackle this issue.

As a student, you can use this application to listen to words and try to spell them. You can then find out where you're going right and where it's going wrong. It also helps you to improve your reading ability. In the other module, you will read handwritten texts and try to spell them correctly. You also have a tutorial that teaches you similar sounding letters or group of letters. Here, there's no one to judge you and the scope of growth is huge!

As a teacher, you can make the practice of your students better. You can add words for both, enhancing the listening and reading skills of kids. Please make sure you add words such that it helps them to learn a lot and at the same time does not demoralise them.

I hope that this software can help both the teachers and students. I would be really happy to hear from you about this application. Please read below for technicalities.

## Development Environment
This software was developed on Ubuntu LTS 20.04 and with Python 3.7.2. 

**Internet connection is necessary for running this software.**

**This version of the software is only meant for running this locally.**

## Software Requirements

### Python 3.7
The software has been developed on Python. So, this is necessary.

If you are having a previous version of Python, then use https://docs.anaconda.com/anaconda/install/ to install Python. Set `activate_base` to `True`. If this is done, then there's no need to set up **virtual environment**.

If you are using pip3, then use this link - https://www.youtube.com/watch?v=N5vscPTWKOk to setup virtual environment and then, install the python packages given below.


### mpg123
This is required for playing sound in the background. 

#### Ubuntu
Press `Ctrl + Alt + T` and then paste this command

`sudo apt-get install mpg123`

Give your password when asked to.

#### macOS
Press `Command+Space` and type Terminal and press enter/return key.

Run in Terminal app:
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null`
and press enter/return key.

If the screen prompts you to enter a password, please enter your Mac's user password to continue. When you type the password, it won't be displayed on screen, but the system would accept it. So just type your password and press ENTER/RETURN key. Then wait for the command to finish.

Run:
`brew install mpg123`

#### Windows
Use this link to download https://www.mpg123.de/download.shtml .

## Required Python packages

### Flask
`conda install -c anaconda flask`

or

`pip3 install flask`

### Pandas
`conda install -c anaconda pandas`

or

`pip3 install pandas`

### gTTS
`pip3 install gTTS`

## Running the software

1) Clone this repository using `git clone https://github.com/smishy05/dyslexhelp.git`

2) Go to the cloned directory and then open the terminal there. 

Just type in `python app.py`. Right click on the link http://127.0.0.1:5000/ and then, click on `Open link`.
