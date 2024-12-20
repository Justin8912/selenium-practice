<div align='center'>
   <img src="https://github.com/user-attachments/assets/503eb767-1bc2-49b0-a223-ca38ad5ec4b4" height="200px"/>
</div>

Selenium Practice
--
The purpose of this repo is to test out selenium for use in automating a small but tedious part of Robin's job. 

There is a section in her job which requires her to manually change the seat count in all sections during registration 
which includes clicking on a set of buttons hundreds of times. This seems like it can be automated. However, due to 
the important nature of this work, there are a couple of guidelines that need to be followed:

1. The modifications need made by the script need to be clear and ideally should be stored in an external file 
2. There should be a way to exclude sections based on time and the unique number of the section 
3. We should be able to see the changes that are being made by the script 

Running tests
--
There is a test react app (`test-react-app`) that is being used to render what the basic display looks like on Robin's side. 

In order to test the selenium app, you must follow these steps:
1. Open one terminal to run the react app and wait until it is fully loaded
2. Open another terminal to run the selenium script

After running the test a directory should populate called `changes` with the time that the file was run 
as the name of the file. This will hold all the record for everything that was changed.

This is mostly just a POC just to make sure I can get this selenium bot running. The general structure of the script 
for the test and for the actual script will look very similar.

Running the bot
--
When you are running the bot you have a couple of options for excluding sections:

1. Exclude by time 
    * Be careful with this selector as it is very lax. For example if you enter 10 here any section with a 10 in the time will be excluded from the bots actions.
2. Exclude by unique number 
    * You can enter one or multiple unique numbers to exclude

The bot runs on Chrome so you will need to have an active sessions for your application in chrome in order for this to run correctly.

Current State
--
Currently the test app will not work with the live environment. This is mainly because I am controlling the display based on state as opposed to routing to new tabs like the ut website does. Since the script is currently working on the UT website, I dont see a reason to over engineer the test app and implement routing. I'll just leave it as is and leave the testing method in case I want to mess around with commands. 

Additionally, there is no _good_ way that I found to bypass MFA, so for now I have added inputs that will wait for user input to tell the script to continue.
