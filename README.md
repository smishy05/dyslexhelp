# dyslexhelp

## Development Environment
This software was developed on Ubuntu LTS 20.04 and with Python 3.7.2. 

## Software Requirements

### Python 3.7
The software has been developed on Python. So, this is necessary.

If you are having a previous version of Python, then use https://docs.anaconda.com/anaconda/install/ to install Python. Set `activate_base` to `True`. If this is done, then there's no need to set up **virtual environment**.

### mgl123
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
