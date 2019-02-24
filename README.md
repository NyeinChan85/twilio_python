
# Twilio_python
---------------

Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs. This particular assignment is done using Python programming lauguage to send text messages from the program to the phone via Twilio. 


## Tools
---------

In order to follow this particular project, you will need to install python and twillio package as follows.

Make sure you are connected to the Internet and your Internet does not block the Python Package Index Server: https://pypi.python.org/pypi that easy_install and pip will connect in order to download Twilio.

## Windows Instructions
-------------------------
•	Make sure your computer's PATH has Python added. This means that in the program Command Prompt you can type the words python and the system knows how to find the python.exe located in your system.
•	If your system does not have Python added to your PATH, it's suggested you reinstall Python and make sure to click on the option to install python to your system PATH when you customize your Python installation:
 
•	Also make sure that your account has Administrative access in order to be able to install programs on your Windows system. If you get permission errors, on Windows, you'll have to close your Command Prompt and open it again as an administrator by right-clicking on it and choosing the appropriate option
•	You can then either type easy_install twilio or pip install twilio to download and install Twilio

## Macintosh and Linux Instruction
------------------------------------
•	Macintosh and Linux systems will already have Python added in their system PATH.
•	Therefore the only step you need to take is to load up the Terminal application and type in sudo easy_install twilio and enter in your password to give easy_install permissions to write to your system folders.
•	If you want to install Twilio with pip, you may need to first install pip on your system because newer Macintosh systems and some Linux distributions may not come with pip installed.
•	Therefore, you should first install pip with sudo easy_install pip
•	You can then use pip to install Twilio with sudo pip install twilio

## Install Verification
------------------------
To check whether Twilio was properly installed, we enter the python command to enter the Python interpreter in the Command Prompt or Terminal application and type in these two commands:
import twilio
print(twilio.__version__)
If it prints a version number, you're almost ready to start sending text. 

## Register your account on www.twilio.com
___________________________________________

Register and get Your Account SID and Auth Token.
Verify your phone number. 
Then, get a new phone number to start expriment with Twilio. 

After you follow all these instructions above, you are ready to run the program

## How to run the program
________________________

In order to run the program, make sure you edit send_text.py, and use the phone number which you'd like to send and use the number you get from Twilio first.
Then, run the program in command prompt or terminal by tying the following command

python send_text.py




